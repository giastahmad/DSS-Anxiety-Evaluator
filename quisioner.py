import streamlit as st
import time
import joblib
import numpy as np
import pickle

class QuisionerPage:
    def __init__(self):
        self.questions = [
            "Saya merasa sulit untuk tenang",
            "Saya merasa mulut saya terasa kering",
            "Saya mengalami kesulitan bernapas (misalnya: napas cepat, sulit bernapas meskipun tidak setelah aktivitas fisik)",
            "Saya cenderung bereaksi berlebihan terhadap situasi",
            "Saya merasa gemetar (misalnya: pada tangan)",
            "Saya merasa sangat gugup",
            "Saya khawatir tentang situasi di mana saya mungkin panik dan mempermalukan diri sendiri",
            "Saya merasa dekat dengan kepanikan",
            "Saya sadar akan detak jantung saya meskipun tidak setelah aktivitas fisik",
            "Saya merasa takut tanpa alasan yang jelas",
            "Saya merasa bahwa hidup itu tidak berarti",
            "Saya merasa diri saya menjadi semakin gelisah",
            "Saya mengalami kesulitan untuk rileks",
            "Saya merasa takut bahwa saya akan 'terhambat' oleh tugas-tugas sepele yang tidak biasa"
        ]
        
        self.choices = [
            "Tidak pernah terjadi pada saya",
            "Terjadi pada saya sampai tingkat tertentu atau kadang-kadang",
            "Terjadi pada saya sampai batas yang cukup berarti atau sering",
            "Sangat sering terjadi pada saya atau hampir selalu"
        ]
        
        if 'current_question' not in st.session_state:
            st.session_state.current_question = 0
        if 'answers' not in st.session_state:
            st.session_state.answers = {}
        if 'user_info' not in st.session_state:
            st.session_state.user_info = {}
            
    def collect_user_info(self):
        """Mengumpulkan informasi dasar pengguna"""
        st.markdown("""
        <div class="question-container">
            <h2>Informasi Pengguna</h2>
            <p>Mohon lengkapi informasi berikut sebelum memulai tes</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Nama")
            age = st.number_input("Usia", min_value=15, max_value=100, value=25)
            
        with col2:
            gender = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
        
        if st.button("Mulai Tes"):
            if name.strip():  # Pastikan nama tidak kosong
                st.session_state.user_info = {
                    "name": name,
                    "age": age,
                    "gender": gender
                }
                st.session_state.show_questions = True
                st.rerun()
            else:
                st.error("Mohon isi nama Anda")

    def predict_anxiety(self):
        """Melakukan prediksi menggunakan model"""
        try:
            # Load model
            with open('Model/knn_anxiety_model.pkl', 'rb') as file:
                model = pickle.load(file)

            answers_array = [st.session_state.answers.get(i, 0) for i in range(len(self.questions))]

            if len(answers_array) != 14:
                st.error("Input data harus memiliki panjang 14.")
                return None, None

            # Reshape data untuk model prediksi
            input_data = np.array(answers_array).reshape(1, -1)

            # Prediksi kategori menggunakan model
            prediction = model.predict(input_data)[0]

            # Hitung probabilitas manual berdasarkan distribusi jawaban
            label_count = [answers_array.count(i) for i in range(4)]  # Hitung jumlah masing-masing label
            total_answers = len(answers_array)
            probability = [count / total_answers for count in label_count]  # Hitung persentase

            return prediction, probability
        except Exception as e:
            st.error(f"Error saat melakukan prediksi: {str(e)}")
            return None, None

    def show_results(self):
        """Menampilkan hasil analisis"""
        st.title("Hasil Analisis Anxiety")
        
        # Tampilkan informasi pengguna
        user_info = st.session_state.user_info
        st.markdown(f"""
        <div style="background: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 10px; margin-bottom: 20px;">
            <h3>Informasi Pengguna</h3>
            <p>Nama: {user_info['name']}</p>
            <p>Usia: {user_info['age']}</p>
            <p>Jenis Kelamin: {user_info['gender']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Lakukan prediksi
        prediction, probability = self.predict_anxiety()
        
        # Tampilkan hasil
        if prediction is not None:
            severity_labels = ['Normal', 'Moderate', 'Severe', 'Extremely Severe']
            severity_labels_id = {
                'Normal': 'Normal',
                'Moderate': 'Sedang',
                'Severe': 'Parah',
                'Extremely Severe': 'Sangat Parah'
            }
            
            # Pilih label berdasarkan probabilitas tertinggi
            max_index = np.argmax(probability)  # Indeks probabilitas tertinggi
            result_label = severity_labels[max_index]
            result_label_id = severity_labels_id[result_label]
            
            color_map = {
                'Normal': '#4CAF50',
                'Moderate': '#ffa500',
                'Severe': '#ff4444',
                'Extremely Severe': '#ff0000'
            }
            
            result_color = color_map[result_label]
            
            probability_list = "".join(
                f"<li>{severity_labels_id[severity_labels[i]]}: {probability[i]*100:.1f}%</li>" 
                for i in range(len(probability))
            )
            
            st.markdown(f"""
            <div style="background: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 10px; margin-bottom: 20px;">
                <h2>Hasil Prediksi</h2>
                <h1 style="color: {result_color};">{result_label_id}</h1>
                <p>Tingkat kecemasan Anda berada pada level {result_label_id.lower()}.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Gagal menampilkan hasil prediksi.")

        if st.button("Kembali ke Beranda", type="primary", use_container_width=True):
            self._reset_state()

    def show(self):
        """Menampilkan halaman kuesioner"""
        st.markdown("""
        <style>
        .question-container {
            background: rgba(255, 255, 255, 0.1);
            padding: 2rem;
            border-radius: 15px;
            margin: 2rem 0;
            animation: fadeIn 0.5s ease-in;
        }
        
        .progress-container {
            margin: 2rem 0;
        }
        
        .choice-button {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 1rem;
            margin: 0.5rem 0;
            border-radius: 10px;
            transition: all 0.3s ease;
        }
        
        .choice-button:hover {
            background: rgba(255, 255, 255, 0.2);
            transform: translateX(10px);
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .nav-buttons {
            display: flex;
            justify-content: space-between;
            margin-top: 2rem;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Cek apakah info pengguna sudah dikumpulkan
        if 'user_info' not in st.session_state or not st.session_state.user_info:
            self.collect_user_info()
            return
        
        # Progress bar
        progress = (st.session_state.current_question + 1) / len(self.questions)
        st.progress(progress)
        st.write(f"Pertanyaan {st.session_state.current_question + 1} dari {len(self.questions)}")
        
        # Question container
        st.markdown(f"""
        <div class="question-container">
            <h2>Pertanyaan {st.session_state.current_question + 1}</h2>
            <p style="font-size: 1.2rem;">{self.questions[st.session_state.current_question]}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Choices
        for i, choice in enumerate(self.choices):
            if st.button(
                choice,
                key=f"choice_{i}",
                use_container_width=True,
            ):
                st.session_state.answers[st.session_state.current_question] = i
                
                # Jika ini pertanyaan terakhir, tampilkan tombol analisis
                if st.session_state.current_question == len(self.questions) - 1:
                    st.session_state.show_analysis_button = True
                else:
                    st.session_state.current_question += 1
                st.rerun()

        # Tombol navigasi
        col1, col2 = st.columns(2)
        
        # Tombol Previous hanya muncul jika bukan pertanyaan pertama
        if st.session_state.current_question > 0:
            with col1:
                if st.button("← Sebelumnya", use_container_width=True):
                    st.session_state.current_question -= 1
                    st.rerun()

        # Tombol Next hanya muncul jika bukan pertanyaan terakhir dan sudah dijawab
        current_answer = st.session_state.answers.get(st.session_state.current_question)
        if st.session_state.current_question < len(self.questions) - 1 and current_answer is not None:
            with col2:
                if st.button("Selanjutnya →", use_container_width=True):
                    st.session_state.current_question += 1
                    st.rerun()

        # Tombol Analisis hanya muncul jika semua pertanyaan sudah dijawab
        if len(st.session_state.answers) == len(self.questions):
            if st.button("Analisis Hasil", type="primary", use_container_width=True):
                st.session_state.page = "result"
                st.rerun()

        # Tombol kembali ke beranda
        st.button("Kembali ke Beranda", key="back_home", on_click=lambda: self._reset_state())

    def _reset_state(self):
        """Helper method untuk mereset state saat kembali ke beranda"""
        st.session_state.page = "home"
        st.session_state.current_question = 0
        st.session_state.answers = {}
        st.session_state.user_info = {}
        st.session_state.show_questions = False
        st.session_state.show_analysis_button = False
        st.rerun()
