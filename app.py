import streamlit as st
import numpy as np
from quisioner import QuisionerPage
from additional_form import ml_context_form, profile_data_form
from result import final_result_page, result_normal


# Page Configuration
st.set_page_config(
    page_title="Anxiety Evaluator & Root Cause Analysis",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# CSS
st.markdown(
    """
<style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        color: white;
    }
    
    .home-container {
        padding: 4rem 2rem;
        max-width: 100vw;
        margin: 0 auto;
        animation: fadeIn 1s ease-in;
    }
    
    .info-box {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 2rem;
        backdrop-filter: blur(10px);
    }
    
    .info-boxes-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.5rem;
        margin-bottom: 2rem;
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
    
    @media (max-width: 768px) {
    .info-boxes-container {
        display: flex;
        flex-direction: column;
    }
    
    .info-box {
        width: 100%;
        margin-bottom: 1rem;
    }
}
</style>
""",
    unsafe_allow_html=True,
)


def home_page():
    st.markdown(
        """
<div class="home-container">
<h1 style="font-size: 3.5rem; text-align: center; margin-bottom: 1rem;">Anxiety Evaluator</h1>
<p style="font-size: 1.2rem; text-align: center; color: #b0b0b0; margin-bottom: 3rem;">
Recognize your anxiety level and find the root cause of it.
</p>

<div class="info-boxes-container">
<div class="info-box">
<h3 style="color: #e0e0e0;">What is Anxiety?</h3>
<p style="color: #b0b0b0; line-height: 1.6;">
Anxiety is a feeling of worry or unease about something that might happen in the future. It often comes with physical signs like muscle tension, faster breathing, and a rapid heartbeat.
It is different from fear. Anxiety is about uncertain or unclear threats in the future, while fear is a short-term response to a clear and immediate danger.
To manage anxiety effectively, it's important to understand its root cause, since addressing what triggers it is the first step toward reducing it.
</p>
</div>

<div class="info-box">
<h3 style="color: #e0e0e0;">About the DASS-42 Test</h3>
<p style="color: #b0b0b0; line-height: 1.6;">
The DASS-42 (Depression Anxiety Stress Scales) is a self-assessment tool used to measure levels of depression, anxiety, and stress. It consists of 42 questions, 
with 14 questions dedicated to each emotional state. This test does not provide a clinical diagnosis, but it helps identify the severity of symptoms and gives insight 
into a person's mental well-being based on how they have felt over the past week. In this application, only the 14 questions related to anxiety are used, allowing for 
a more focused and efficient assessment of an individual's anxiety level.
</p>
</div>

<div class="info-box">
<h3 style="color: #e0e0e0;">Disclaimer !!</h3>
<p style="color: #b0b0b0; line-height: 1.6;">
This application is not a medical diagnostic tool and does not replace professional healthcare advice. The results are for informational purposes only. For accurate evaluation, 
diagnosis, or treatment, please consult a licensed psychologist, psychiatrist, or other healthcare professional. Use this application as a supportive guide to help you make more 
informed decisions about your well-being, not as a definitive medical conclusion.
</p>
</div>
</div>
</div>
    """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown(
            """
<div class="feature-box animated" style="animation-delay: 0.4s;">
<div>
<div class="feature-icon">📝</div>
<div class="feature-title">Start Anxiety Test</div>
<div class="feature-description">Take the DASS-42 test to understand your anxiety level</div>
</div>
</div>
        """,
            unsafe_allow_html=True,
        )
        if st.button(
            "Start Test", key="test", type="primary", use_container_width=True
        ):
            st.session_state.page = "profile_form"
            st.rerun()


def main():
    if "page" not in st.session_state:
        st.session_state.page = "home"

    if st.session_state.page == "home":
        home_page()
    elif st.session_state.page == "quisioner":
        quisioner = QuisionerPage()
        quisioner.show()
    elif st.session_state.page == "profile_form":
        profile_data_form()
    elif st.session_state.page == "ml_context_form":
        ml_context_form()
    elif st.session_state.page == "final_result_normal":
        result_normal()
    elif st.session_state.page == "result":
        final_result_page()


if __name__ == "__main__":
    main()
