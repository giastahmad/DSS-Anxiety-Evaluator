import streamlit as st

def quisioner_page():
    st.title("Halaman Kuisioner")
    st.write("Silakan isi pertanyaan berikut:")
    

    
    # Tombol untuk mengirim jawaban
    if st.button("Kirim"):
        st.success("Jawaban Anda telah dikirim.")
        
    st.button("Kembali ke Home", on_click=lambda: st.session_state.update({"page": "home"}))
