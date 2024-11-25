import streamlit as st
from quisioner import QuisionerPage
import time

# Konfigurasi halaman
st.set_page_config(
    page_title="Cek Tingkat Anxiety", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS untuk styling
st.markdown("""
<style>
    /* Global styles */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        color: white;
    }
    
    /* Home page styles */
    .home-container {
        height: 50vh;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 2rem;
    }
    
    .welcome-section {
        text-align: center;
        margin-top: 4rem;
        animation: fadeIn 1s ease-in;
    }
    
    .feature-box {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 2rem;
        height: 300px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        cursor: pointer;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        text-align: center;
        margin: 1rem;
        backdrop-filter: blur(10px);
    }
    
    .feature-box:hover {
        transform: translateY(-10px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.4);
        background: rgba(255, 255, 255, 0.08);
    }
    
    .feature-icon {
        font-size: 48px;
        margin-bottom: 1rem;
    }
    
    .feature-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 1rem;
        color: #e0e0e0;
    }
    
    .feature-description {
        font-size: 16px;
        margin-bottom: 1rem;
        color: #b0b0b0;
    }

    .custom-button {
        background: #6a1b9a;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        color: white;
        cursor: pointer;
        transition: background 0.3s ease;
        width: 100%;
        margin-top: 1rem;
    }

    .custom-button:hover {
        background: #8e24aa;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes slideUp {
        from { transform: translateY(50px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    
    .animated {
        animation: slideUp 0.5s ease-out;
    }
</style>
""", unsafe_allow_html=True)

def home_page():
    # Welcome section
    st.markdown("""
        <div class="home-container">
            <div class="welcome-section">
                <h1 style="font-size: 3.5rem; margin-bottom: 1rem; color: #e0e0e0;">Selamat Datang di Anxiety Evaluator</h1>
                <p style="font-size: 1.2rem; color: #b0b0b0;">Kenali tingkat kondisi gangguan kecemasan (anxiety) anda</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="feature-box animated" style="animation-delay: 0.2s;">
                <div>
                    <div class="feature-icon">📊</div>
                    <div class="feature-title">Statistik Anxiety</div>
                    <div class="feature-description">Lihat tren dan statistik anxiety di berbagai kelompok usia</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Lihat Statistik", key="stats", type="primary", use_container_width=True):
            st.session_state.page = "statistics"
            st.rerun()

    with col2:
        st.markdown("""
            <div class="feature-box animated" style="animation-delay: 0.4s;">
                <div>
                    <div class="feature-icon">📝</div>
                    <div class="feature-title">Mulai Tes Anxiety</div>
                    <div class="feature-description">Ikuti tes DASS-42 untuk mengetahui tingkat kecemasan Anda</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Mulai Tes", key="test", type="primary", use_container_width=True):
            st.session_state.page = "quisioner"
            st.rerun()

    with col3:
        st.markdown("""
            <div class="feature-box animated" style="animation-delay: 0.6s;">
                <div>
                    <div class="feature-icon">ℹ️</div>
                    <div class="feature-title">Informasi</div>
                    <div class="feature-description">Pelajari lebih lanjut tentang anxiety dan cara mengatasinya</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Pelajari", key="info", type="primary", use_container_width=True):
            st.session_state.page = "information"
            st.rerun()

def main():
    if 'page' not in st.session_state:
        st.session_state.page = "home"

    if st.session_state.page == "home":
        home_page()
    elif st.session_state.page == "quisioner":
        quisioner = QuisionerPage()
        quisioner.show()
    elif st.session_state.page in ["statistics", "information"]:
        st.title(f"Halaman {st.session_state.page}")
        st.write("Halaman ini sedang dalam pengembangan")
        if st.button("Kembali ke Beranda", type="primary"):
            st.session_state.page = "home"
            st.rerun()

if __name__ == "__main__":
    main()