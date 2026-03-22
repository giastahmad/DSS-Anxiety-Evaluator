import streamlit as st
import pandas as pd
import joblib

import streamlit as st
import pandas as pd
import joblib
import json
import google.generativeai as genai

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)

def final_result_page():
    st.title("Anxiety & Trigger Analysis Results")
    
    dass_level = st.session_state.get('dass_result', 'Moderate') 
    
    if dass_level == "Mild": color_code = "#FFC107"
    elif dass_level == "Moderate": color_code = "#FF9800"
    elif dass_level == "Severe": color_code = "#F44336"
    elif dass_level == "Extremely Severe": color_code = "#8B0000"
    else: color_code = "#9E9E9E"

    st.markdown(f"""
    <div style="background: rgba(255, 255, 255, 0.05); border-radius: 10px; padding: 1.5rem; margin-bottom: 2rem;">
        <h3 style="color: {color_code}; margin: 0; font-weight: bold;">Your Anxiety Level: {dass_level}</h3>
        <p style="color: #b0b0b0; margin-top: 0.5rem; margin-bottom: 0;">Measured by DASS-42 Clinical Standard</p>
    </div>
    """, unsafe_allow_html=True)
    
    profile_data = st.session_state.get('profile_data', {})
    ml_data = st.session_state.get('ml_data', {})
    user_data = {**profile_data, **ml_data}
    
    if not user_data:
        st.error("Incomplete data. Please fill out the form from the beginning.")
        return

    df_input = pd.DataFrame([user_data])
    drop_columns = ['Age', 'Gender', 'Education', 'Country']
    df_model = df_input.drop(columns=[col for col in drop_columns if col in df_input.columns])
    
    for col in df_model.select_dtypes(include=['object']).columns:
        df_model[col] = df_model[col].astype('category')

    main_causes = []
    try:
        model = joblib.load('Model/cause_analysis_model.pkl')
        probability = model.predict_proba(df_model)[0]
        class_list = model.classes_
        
        prediction_result = dict(zip(class_list, probability))
        
        def class_name_clean(raw_name):
            name_str = str(raw_name)
            
            if name_str == '0': return 'Work'
            elif name_str == '1': return 'Financial'
            elif name_str == '2': return 'Social'
            elif name_str == '3': return 'Lifestyle'
            
            else: return name_str.replace('_Score', '')
        
        for class_name, prob in prediction_result.items():
            if prob >= 0.25:
                clean_name = class_name_clean(class_name)
                if clean_name == 'Work':
                    clean_name = 'Work / Academic'
                main_causes.append(clean_name)
                
        if not main_causes:
            top_cause_raw = max(prediction_result, key=prediction_result.get)
            top_cause = class_name_clean(top_cause_raw)
            main_causes.append('Work / Academic' if top_cause == 'Work' else top_cause)

    except Exception as e:
        st.error(f"Error processing ML model: {e}")
        return

    llm_context = {
        "user_demographics": {
            "age": user_data.get('Age'),
            "gender": user_data.get('Gender'),
            "marital_status": user_data.get('Marital_Status'),
            "employment_status": user_data.get('Employment_Status'),
            "country": user_data.get('Country')
        },
        "clinical_result": {
            "dass_42_level": dass_level
        },
        "machine_learning_analysis": {
            "main_stress_triggers": main_causes
        }
    }

    prompt_llm = f"""
    Act as an empathetic and supportive mental health assistant. 
    Do NOT act as a doctor, do NOT diagnose, and do NOT prescribe medication.

    Here is the user's context in JSON format:
    {json.dumps(llm_context, indent=2)}

    Task:
    Write a warm, highly personalized 1-paragraph closing message for this user in English. 
    - Validate their feelings based on their specific demographics and triggers.
    - Give a gentle, practical word of encouragement or a simple coping mechanism suggestion suitable for their situation. Tone: Supportive, conversational, not clinical.
    """

    st.markdown("""<h3 style="color: #e0e0e0;">Personalized Suggestion</h3>""", unsafe_allow_html=True)
    
    with st.spinner("Analyzing your profile and generating personalized advice..."):
        try:
            genai_model = genai.GenerativeModel('gemini-2.5-flash')
            response = genai_model.generate_content(prompt_llm)
            llm_text = response.text
        except Exception as e:
            llm_text = "Sorry, our AI support system is busy. But remember, you've already made a great move by recognizing your condition today."
            print(f"Gemini API Error: {e}")

    st.markdown(f"""
    <div style="background: rgba(255, 255, 255, 0.05); border-radius: 15px; padding: 2rem; margin-bottom: 2rem; line-height: 1.6; color: #e0e0e0;">
        {llm_text}
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Back to Homepage", type="primary"):
        st.session_state.clear()
        st.session_state.page = "home"
        st.rerun()
        
def result_normal():
    st.title("Anxiety & Trigger Analysis Results")
    
    st.success("Your Anxiety Level: Normal")
    
    st.markdown("""
    <div class="info-box">
        <h4>Congrats!</h4>
        <p>Good news! Based on the DASS-42 evaluation, your mental state and anxiety levels are within normal and healthy limits. You manage stress very well.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Back to Homepage", type="primary"):
        st.session_state.clear()
        st.session_state.page = "home"
        st.rerun()