import streamlit as st
import time
import pandas as pd
import joblib
import numpy as np

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
        
        # Inisialisasi state
        if 'current_question' not in st.session_state:
            st.session_state.current_question = 0
        if 'answers' not in st.session_state:
            st.session_state.answers = {}
        if 'user_info' not in st.session_state:
            st.session_state.user_info = {}
            
    def collect_user_info(self):
        """Mengumpulkan informasi tambahan dari pengguna untuk input model"""
        st.markdown("""
        <div class="question-container">
            <h2>Informasi Tambahan</h2>
            <p>Mohon lengkapi informasi berikut untuk analisis yang lebih akurat</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.number_input("Usia", min_value=15, max_value=100, value=25)
            gender = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
            sleep_hours = st.number_input("Rata-rata jam tidur per hari", min_value=0, max_value=24, value=7)
            
        with col2:
            exercise_frequency = st.selectbox("Frekuensi olahraga per minggu", 
                                            ["Tidak pernah", "1-2 kali", "3-4 kali", "5 kali atau lebih"])
            stress_level = st.slider("Tingkat stress (1-10)", min_value=1, max_value=10, value=5)
            has_history = st.checkbox("Memiliki riwayat anxiety sebelumnya")
        
        if st.button("Lanjutkan ke Kuesioner"):
            st.session_state.user_info = {
                "age": age,
                "gender": 1 if gender == "Laki-laki" else 0,
                "sleep_hours": sleep_hours,
                "exercise_freq": ["Tidak pernah", "1-2 kali", "3-4 kali", "5 kali atau lebih"].index(exercise_frequency),
                "stress_level": stress_level,
                "has_history": int(has_history)
            }
            st.session_state.show_questions = True
            st.rerun()

    def prepare_model_input(self):
        """Menyiapkan data untuk input ke model AI"""
        # Mengambil jawaban kuesioner
        answers_array = [st.session_state.answers[i] for i in range(14)]
        
        # Menghitung fitur-fitur tambahan dari jawaban
        features = {
            # Fitur dasar dari info pengguna
            "age": st.session_state.user_info["age"],
            "gender": st.session_state.user_info["gender"],
            "sleep_hours": st.session_state.user_info["sleep_hours"],
            "exercise_freq": st.session_state.user_info["exercise_freq"],
            "stress_level": st.session_state.user_info["stress_level"],
            "has_history": st.session_state.user_info["has_history"],
            
            # Fitur dari jawaban kuesioner
            "total_score": sum(answers_array),
            "avg_score": np.mean(answers_array),
            "max_score": max(answers_array),
            "physical_symptoms": np.mean([answers_array[i] for i in [1, 2, 4, 8]]),  # Gejala fisik
            "emotional_symptoms": np.mean([answers_array[i] for i in [0, 3, 5, 9]]),  # Gejala emosional
            "behavioral_symptoms": np.mean([answers_array[i] for i in [6, 7, 10, 11, 12, 13]]),  # Gejala perilaku
            "variance_score": np.var(answers_array)
        }
        
        return pd.DataFrame([features])

    def predict_anxiety(self, model_input):
        """Melakukan prediksi menggunakan model Random Forest"""
        try:
            # Load model
            model = joblib.load('anxiety_model.joblib')
            
            # Prediksi
            prediction = model.predict(model_input)
            probability = model.predict_proba(model_input)
            
            return prediction[0], probability[0]
            
        except Exception as e:
            st.error(f"Error saat melakukan prediksi: {str(e)}")
            return None, None

    def show_results(self):
        """Menampilkan hasil analisis"""
        st.title("Hasil Analisis Anxiety")
        
        # Persiapkan data untuk model
        model_input = self.prepare_model_input()
        
        # Lakukan prediksi
        prediction, probability = self.predict_anxiety(model_input)
        
        # Tampilkan hasil
        st.markdown("""
        <div class="result-container" style="animation: fadeIn 1s ease-in;">
            <h2>Hasil Analisis AI</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Tampilkan visualisasi dan interpretasi
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Tingkat Anxiety")
            if prediction is not None:
                severity_labels = ["Normal", "Ringan", "Sedang", "Parah", "Sangat Parah"]
                st.markdown(f"<h1 style='color: #4CAF50;'>{severity_labels[prediction]}</h1>", 
                          unsafe_allow_html=True)
                
                # Tampilkan probabilitas untuk setiap kelas
                st.subheader("Probabilitas per Kategori:")
                for label, prob in zip(severity_labels, probability):
                    st.write(f"{label}: {prob:.2%}")
        
        with col2:
            st.subheader("Analisis Gejala")
            model_input = model_input.iloc[0]
            
            # Visualisasi distribusi gejala
            st.write("Distribusi Gejala:")
            st.write(f"- Gejala Fisik: {model_input['physical_symptoms']:.2f}")
            st.write(f"- Gejala Emosional: {model_input['emotional_symptoms']:.2f}")
            st.write(f"- Gejala Perilaku: {model_input['behavioral_symptoms']:.2f}")
        
        # Rekomendasi berdasarkan prediksi
        st.subheader("Rekomendasi")
        if prediction == 0:
            st.write("Tingkat anxiety Anda normal. Tetap jaga pola hidup sehat dan kelola stress dengan baik.")
        elif prediction == 1:
            st.write("Anda mengalami anxiety ringan. Cobalah teknik relaksasi dan meditasi.")
        elif prediction == 2:
            st.write("Anda mengalami anxiety sedang. Disarankan untuk berkonsultasi dengan profesional.")
        else:
            st.write("Anda mengalami anxiety parah. Sangat disarankan untuk segera mencari bantuan profesional.")
        
        # Tombol navigasi
        if st.button("Mulai Tes Baru"):
            st.session_state.current_question = 0
            st.session_state.answers = {}
            st.session_state.user_info = {}
            st.rerun()
        
        if st.button("Kembali ke Beranda"):
            st.session_state.page = "home"
            st.session_state.current_question = 0
            st.session_state.answers = {}
            st.session_state.user_info = {}
            st.rerun()

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
        </style>
        """, unsafe_allow_html=True)

        # Header
        st.title("Tes Anxiety DASS-42")
        
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
                time.sleep(0.3)  # Slight delay for animation effect
                if st.session_state.current_question < len(self.questions) - 1:
                    st.session_state.current_question += 1
                    st.rerun()
                else:
                    self.show_results()
        
        # Navigation buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.session_state.current_question > 0:
                if st.button("← Pertanyaan Sebelumnya"):
                    st.session_state.current_question -= 1
                    st.rerun()
        
        # Back to home button
        if st.button("Kembali ke Beranda"):
            st.session_state.page = "home"
            st.session_state.current_question = 0
            st.session_state.answers = {}
            st.session_state.user_info = {}
            st.rerun()