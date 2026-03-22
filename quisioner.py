import streamlit as st
import numpy as np
import pickle


class QuisionerPage:
    def __init__(self):
        self.questions = [
            "I found it hard to wind down",
            "I experienced dryness of my mouth",
            "I experienced breathing difficulty (even in the absence of physical exertion)",
            "I tended to over-react to situations",
            "I experienced trembling (e.g., in the hands)",
            "I felt very nervous",
            "I was worried about situations in which I might panic and make a fool of myself",
            "I felt I was close to panic",
            "I was aware of the action of my heart in the absence of physical exertion",
            "I felt scared without any good reason",
            "I felt that life was meaningless",
            "I found myself getting agitated",
            "I found it difficult to relax",
            "I feared that I would be 'thrown' by some trivial tasks",
        ]

        self.choices = ["Never", "Sometimes", "Often", "Almost always"]
        
        if 'current_question' not in st.session_state:
            st.session_state.current_question = 0
        if 'answers' not in st.session_state:
            st.session_state.answers = {}
            

    def show(self):
        st.markdown(
            """
        <style>
        .question-container {
            background: rgba(255, 255, 255, 0.05);
            padding: 2rem;
            border-radius: 15px;
            margin: 1rem 0;
            border: 1px solid rgba(255,255,255,0.1);
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        </style>
        """,
            unsafe_allow_html=True,
        )
        st.title("DASS-42 Quisioner (Anxiety Assessment)")
        st.write("")

        # Progress bar
        progress = (st.session_state.current_question + 1) / len(self.questions)
        st.progress(progress)
        q_idx = st.session_state.current_question

        col1, col2 = st.columns(2)

        with col1:
            # Question container
            st.markdown(
                f"""
            <div class="question-container">
                <h1>Question {q_idx + 1} of {len(self.questions)}</h1>
                <p style="font-size: 2.2rem;">{self.questions[q_idx]}</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with col2:
            # Choices
            st.write("")
            for i, choice in enumerate(self.choices):
                if st.button(choice, key=f"dass_{q_idx}_{i}", use_container_width=True):
                    st.session_state.answers[q_idx] = i

                    if q_idx == len(self.questions) - 1:
                        total_skor = sum(st.session_state.answers.values())
                        st.session_state.dass_result = self.mapping_dass_result(total_skor)
                        if st.session_state.dass_result in ["Mild", "Moderate", "Severe", "Extremely Severe"]:
                            st.session_state.page = "ml_context_form"
                        else:
                            st.session_state.page = "final_result_normal"
                    else:
                        st.session_state.current_question += 1
                    st.rerun()
                    
    def mapping_dass_result(self, total_score):
        if total_score <= 7:
            return "Normal"
        elif total_score <= 9:
            return "Mild"
        elif total_score <= 14:
            return "Moderate"
        elif total_score <= 19:
            return "Severe"
        else:
            return "Extremely Severe"