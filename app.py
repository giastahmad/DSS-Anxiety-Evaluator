# import streamlit as st
# from quisioner import quisioner_page

# # Konfigurasi halaman
# st.set_page_config(page_title="Cek Tingkat Anxiety", layout="wide")

# # CSS Styling dengan tambahan styling untuk button
# st.markdown("""
#     <style>
#     .centered-title {
#         text-align: center;
#         font-size: 48px;
#         color: #ffffff;
#         font-weight: bold;
#         margin-bottom: 30px;
#     }
    
#     /* Custom Large Button Styles */
#     .stButton > button {
#         width: 100%;
#         height: 200px;  /* Tinggi yang sama dengan banner container sebelumnya */
#         font-size: 32px !important;
#         font-weight: bold;
#         color: white !important;
#         background-color: #4CAF50 !important;
#         border-radius: 15px !important;
#         transition: background-color 0.3s ease !important;
#     }
    
#     .stButton > button:hover {
#         background-color: #45a049 !important;
#     }
    
#     /* Responsive adjustments */
#     @media (max-width: 768px) {
#         .stButton > button {
#             height: 150px;
#             font-size: 24px !important;
#         }
#     }
#     </style>
#     """, 
#     unsafe_allow_html=True
# )

# # Halaman Home
# def home_page():
#     st.markdown(
#         "<h1 class='centered-title'>Selamat Datang di Website Cek Tingkat Anxiety</h1>",
#         unsafe_allow_html=True,
#     )

#     # Layout dengan tiga kolom
#     col1, col2, col3 = st.columns(3)

#     with col1:
#         st.button("Fitur 2", key="feature2", on_click=lambda: st.session_state.update({"page": "home"}))

#     with col2:
#         st.button("Mulai Kuisioner", key="start_quiz", on_click=lambda: st.session_state.update({"page": "quisioner"}))
            

#     with col3:
#         st.button("Fitur 3", key="feature3", on_click=lambda: st.session_state.update({"page": "home"}))

# # Routing Halaman Utama
# def main():
#     if 'page' not in st.session_state:
#         st.session_state.page = "home"

#     if st.session_state.page == "home":
#         home_page()
#     elif st.session_state.page == "quisioner":
#         quisioner_page()
#     else:
#        st.write("Halaman yang Anda cari belum tersedia.")
# # Jalankan aplikasi
# if __name__ == "__main__":
#     main()


#==============================================================================================#

# import streamlit as st
# from quisioner import quisioner_page

# # Konfigurasi halaman
# st.set_page_config(page_title="Cek Tingkat Anxiety", layout="wide")

# # CSS Styling khusus untuk tombol besar di home
# st.markdown("""
#     <style>
#     .centered-title {
#         text-align: center;
#         font-size: 48px;
#         color: #ffffff;
#         font-weight: bold;
#         margin-bottom: 30px;
#     }
    
#     /* Styling khusus untuk tombol besar di home */
#     .home-large-button {
#         width: 100%;
#         height: 200px !important;
#         font-size: 32px !important;
#         font-weight: bold !important;
#         color: white !important;
#         background-color: #4CAF50 !important;
#         border-radius: 15px !important;
#         transition: background-color 0.3s ease !important;
#         white-space: normal !important;
#         display: flex !important;
#         align-items: center !important;
#         justify-content: center !important;
#     }
    
#     .home-large-button:hover {
#         background-color: #45a049 !important;
#     }
    
#     /* Responsive adjustments */
#     @media (max-width: 768px) {
#         .home-large-button {
#             height: 150px !important;
#             font-size: 24px !important;
#         }
#     }
#     </style>
#     """, 
#     unsafe_allow_html=True
# )

# # Halaman Home
# def home_page():
#     st.markdown(
#         "<h1 class='centered-title'>Selamat Datang di Website Cek Tingkat Anxiety</h1>",
#         unsafe_allow_html=True,
#     )

#     # Layout dengan tiga kolom
#     col1, col2, col3 = st.columns(3)

#     with col1:
#         # Tambahkan class CSS khusus
#         st.markdown('''
#         <button class="home-large-button stButton" 
#                 onclick="window.location.href='#feature2'">
#             Fitur 2
#         </button>
#         ''', unsafe_allow_html=True)

#     with col2:
#         # Tambahkan class CSS khusus
#         st.markdown('''
#         <button class="home-large-button stButton" 
#                 onclick="window.location.href='#quisioner'">
#             Mulai Kuisioner
#         </button>
#         ''', unsafe_allow_html=True)

#     with col3:
#         # Tambahkan class CSS khusus
#         st.markdown('''
#         <button class="home-large-button stButton" 
#                 onclick="window.location.href='#feature3'">
#             Fitur 3
#         </button>
#         ''', unsafe_allow_html=True)

# # Routing Halaman Utama
# def main():
#     if 'page' not in st.session_state:
#         st.session_state.page = "home"

#     if st.session_state.page == "home":
#         home_page()
#     elif st.session_state.page == "quisioner":
#         quisioner_page()
#     else:
#        st.write("Halaman yang Anda cari belum tersedia.")

# # Jalankan aplikasi
# if __name__ == "__main__":
#     main()
#=====================================================================================================#

import streamlit as st
from quisioner import quisioner_page

# Konfigurasi halaman
st.set_page_config(page_title="Cek Tingkat Anxiety", layout="wide")

# CSS Styling khusus untuk tombol besar di home
st.markdown("""
    <style>
    .centered-title {
        text-align: center;
        font-size: 48px;
        color: #ffffff;
        font-weight: bold;
        margin-bottom: 30px;
    }
    
    /* Styling khusus untuk tombol besar di home */
    .home-large-button {
        width: 100%;
        height: 200px !important;
        font-size: 32px !important;
        font-weight: bold !important;
        color: white !important;
        background-color: #4CAF50 !important;
        border-radius: 15px !important;
        transition: background-color 0.3s ease !important;
        white-space: normal !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    
    .home-large-button:hover {
        background-color: #45a049 !important;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .home-large-button {
            height: 150px !important;
            font-size: 24px !important;
        }
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Fungsi untuk mengatur halaman
def set_page(page_name):
    st.session_state.page = page_name

# Halaman Home
def home_page():
    st.markdown(
        "<h1 class='centered-title'>Selamat Datang di Website Cek Tingkat Anxiety</h1>",
        unsafe_allow_html=True,
    )

    # Layout dengan tiga kolom
    col1, col2, col3 = st.columns(3)

    with col1:
        # Tombol Fitur 2 dengan navigasi menggunakan session_state
        if st.button("Fitur 2", key="feature2", 
                     help="Klik untuk menuju Fitur 2",
                     use_container_width=True,
                     type="primary"):
            set_page("feature2")
            st.rerun()

    with col2:
        # Tombol Mulai Kuisioner dengan navigasi menggunakan session_state
        if st.button("Mulai Kuisioner", key="start_quiz", 
                     help="Klik untuk memulai kuisioner",
                     use_container_width=True,
                     type="primary"):
            set_page("quisioner")
            st.rerun()

    with col3:
        # Tombol Fitur 3 dengan navigasi menggunakan session_state
        if st.button("Fitur 3", key="feature3", 
                     help="Klik untuk menuju Fitur 3",
                     use_container_width=True,
                     type="primary"):
            set_page("feature3")
            st.rerun()

# Fungsi untuk halaman Fitur 2
def feature2_page():
    st.title("Fitur 2")
    if st.button("Kembali ke Beranda"):
        set_page("home")
        st.rerun()

# Fungsi untuk halaman Fitur 3
def feature3_page():
    st.title("Fitur 3")
    if st.button("Kembali ke Beranda"):
        set_page("home")
        st.rerun()

# Inisialisasi session_state untuk page jika belum ada
if 'page' not in st.session_state:
    st.session_state.page = "home"

# Routing berdasarkan page di session_state
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "quisioner":
    quisioner_page()
elif st.session_state.page == "feature2":
    feature2_page()
elif st.session_state.page == "feature3":
    feature3_page()
else:
    st.write("Halaman yang Anda cari belum tersedia.")