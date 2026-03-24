import streamlit as st

def profile_data_form():
    st.title("Please enter your personal information.")
    st.markdown(
        """
        The data you provide is guaranteed to be confidential and will only be used for the purpose of analyzing your anxiety levels.
    """
    )
    
    if "profile_data" not in st.session_state:
        st.session_state.profile_data = {}
    
    st.subheader("Profile Information")
    col1, col2 = st.columns(2)
    st.session_state.profile_data["Age"] = col1.number_input(
        "What is your age?", 15, 100
    )
    st.session_state.profile_data["Gender"] = col2.selectbox(
        "Gender", ["Male", "Female", "Prefer not to say"], index=None
    )
    
    col3, col4 = st.columns(2)
    st.session_state.profile_data["Education"] = col3.selectbox(
        "Highest Education Level",
        ["High School", "Bachelor", "Master", "PhD"], index=None
    )
    st.session_state.profile_data["Marital_Status"] = col4.selectbox(
        "Marital Status (If you have a partner, e.g., dating or engaged, please select 'Married')", ["Single", "Married", "Divorced", "Widowed"]
    )
    st.session_state.profile_data["Country"] = st.text_input(
        "Country of Residence", "", placeholder="e.g., Indonesia, USA, etc."
    )
    emp_status = st.selectbox(
        "What is your primary activity at the moment? (If you are both studying and working, choose a working option)",
        ["Full-time", "Part-time", "Student", "Unemployed", "Self-employed"]
    )
    st.session_state.profile_data["Employment_Status"] = emp_status
    
    st.write("")
    
    next_btn = st.button(
            "Next", type="primary", use_container_width=True
        )
    if next_btn:
        st.session_state.page = "quisioner"
        st.rerun()
        
def activities_and_finance_page():
    st.title("Activities & Finances")
    st.markdown(
        """
        The data you provide is guaranteed to be confidential and will only be used for the purpose of analyzing your anxiety levels.
    """
    )
    
    if "ml_data" not in st.session_state:
        st.session_state.ml_data = {}
        
    emp_status = st.session_state.profile_data.get("Employment_Status", "Unemployed")
    st.session_state.ml_data["Employment_Status"] = emp_status

    if emp_status in ["Full-time", "Part-time", "Student", "Self-employed"]:
        label_act = "work" if emp_status in ["Full-time", "Part-time", "Self-employed"] else "college activities/assignments"
        institution_label = "workplace" if emp_status in ["Full-time", "Part-time", "Self-employed"] else "school/university"

        c1, c2 = st.columns(2)
        
        mh_options = ["Yes", "No", "Not Sure"]
        saved_mh = st.session_state.ml_data.get("Company_Mental_Health_Support", "No")
        st.session_state.ml_data["Company_Mental_Health_Support"] = c1.selectbox(
            f"Does your {institution_label} provide mental health support or counseling services?",
            mh_options, index=mh_options.index(saved_mh)
        )
       
        remote_options = ["Yes", "Hybrid", "No"]
        saved_remote = st.session_state.ml_data.get("Remote_Work", "No")
        st.session_state.ml_data["Remote_Work"] = c2.selectbox(
            f"Do you usually do your {label_act} remotely (from home)?",
            remote_options, index=remote_options.index(saved_remote)
        )

        st.session_state.ml_data["Job_Satisfaction"] = st.slider(
            f"How satisfied are you with your current {label_act}? (0 = Very dissatisfied, 10 = Very satisfied)", 
            0, 10, value=st.session_state.ml_data.get("Job_Satisfaction", 5)
        )
        st.session_state.ml_data["Work_Stress_Level"] = st.slider(
            f"How stressful do you find your {label_act}? (0 = Very relaxed, 10 = Extremely stressful)", 
            0, 10, value=st.session_state.ml_data.get("Work_Stress_Level", 5)
        )
        st.session_state.ml_data["Work_Life_Balance"] = st.slider(
            "How well are you able to balance your responsibilities and personal time? (0 = Very poor, 10 = Very balanced)", 
            0, 10, value=st.session_state.ml_data.get("Work_Life_Balance", 5)
        )
        st.session_state.ml_data["Work_Hours_Per_Week"] = st.slider(
            f"How many hours do you spend on {label_act} per week?", 
            0, 100, value=st.session_state.ml_data.get("Work_Hours_Per_Week", 40)
        )
        
        bully_options = ["No", "Yes"]
        saved_bully = "Yes" if st.session_state.ml_data.get("Ever_Bullied_At_Work", 0) == 1 else "No"
        bully = st.radio(
            "Have you ever felt excluded, discriminated against, or bullied in your work/school environment?",
            bully_options, index=bully_options.index(saved_bully)
        )
        st.session_state.ml_data["Ever_Bullied_At_Work"] = 1 if bully == "Yes" else 0

    st.divider()
    
    income_options = ["Low (Often insufficient)", "Medium (Adequate)", "High (Very sufficient)"]
    saved_income = st.session_state.ml_data.get("Income_UI", "Medium (Adequate)")
    
    income_ui = st.selectbox(
        "How would you describe your current financial situation?",
        income_options, index=income_options.index(saved_income)
    )
    st.session_state.ml_data["Income_UI"] = income_ui
    
    st.session_state.ml_data["Financial_Stress"] = st.slider(
        "How often do you feel stressed or anxious about money, bills, or living expenses? (0 = Never, 10 = Constantly)", 
        0, 10, value=st.session_state.ml_data.get("Financial_Stress", 5)
    )
    
    st.write("")
    
    if st.button("Next", type="primary", use_container_width=True):
        st.session_state.page = "social_life"
        st.rerun()


def social_life_page():
    st.title("Social Life & Support")
    st.markdown(
        """
        The data you provide is guaranteed to be confidential and will only be used for the purpose of analyzing your anxiety levels.
    """
    )
    
    st.session_state.ml_data["Close_Friends_Count"] = st.number_input(
        "How many close friends do you have (who you can rely on during difficult times)?", 
        0, 15, value=st.session_state.ml_data.get("Close_Friends_Count", 2)
    )
    st.session_state.ml_data["Social_Support"] = st.slider(
        "How much emotional support do you feel you receive from family and friends? (0 = None, 10 = A lot)", 
        0, 10, value=st.session_state.ml_data.get("Social_Support", 5)
    )
    st.session_state.ml_data["Feel_Understood"] = st.slider(
        "How often do you feel truly understood by others? (0 = Never, 10 = Always)", 
        0, 10, value=st.session_state.ml_data.get("Feel_Understood", 5)
    )
    st.session_state.ml_data["Loneliness"] = st.slider(
        "How often do you feel lonely, even when you are around others? (0 = Never, 10 = Always)", 
        0, 10, value=st.session_state.ml_data.get("Loneliness", 5)
    )
    
    discuss_options = ["Never (Keep it to myself)", "Rarely", "Sometimes", "Very easily"]
    saved_discuss = st.session_state.ml_data.get("Discuss_UI", "Sometimes")
    
    discuss_ui = st.selectbox(
        "How comfortable are you talking about your feelings or stress with others?",
        discuss_options, index=discuss_options.index(saved_discuss)
    )
    st.session_state.ml_data["Discuss_UI"] = discuss_ui

    st.write("")
    col1, col2 = st.columns(2)
    if col1.button("Back", key="back_soc", use_container_width=True):
        st.session_state.page = "activities_finance"
        st.rerun()
    if col2.button("Next", key="next_soc", type="primary", use_container_width=True):
        st.session_state.page = "lifestyle"
        st.rerun()


def lifestyle_page():
    st.title("Lifestyle & Habits")
    st.markdown(
        """
        The data you provide is guaranteed to be confidential and will only be used for the purpose of analyzing your anxiety levels.
    """
    )
    
    c1, c2 = st.columns(2)
    st.session_state.ml_data["Sleep_Hours_Night"] = c1.slider(
        "How many hours of sleep do you get per night on average?", 
        0.0, 24.0, value=float(st.session_state.ml_data.get("Sleep_Hours_Night", 7.0))
    )
    st.session_state.ml_data["Caffeine_Drinks_Day"] = c2.slider(
        "How many cups of caffeinated beverages do you consume per day?", 
        0, 10, value=int(st.session_state.ml_data.get("Caffeine_Drinks_Day", 1))
    )

    ex_options = ["Never", "1-2 Times", "3-4 Times", "5+ Times"]
    saved_ex = st.session_state.ml_data.get("Exercise_Per_Week", "1-2 Times")
    st.session_state.ml_data["Exercise_Per_Week"] = st.selectbox(
        "How many times do you exercise per week?", 
        ex_options, index=ex_options.index(saved_ex)
    )
    
    diet_options = ["Poor", "Average", "Good", "Excellent"]
    saved_diet = st.session_state.ml_data.get("Diet_Quality", "Average")
    st.session_state.ml_data["Diet_Quality"] = st.selectbox(
        "How would you rate the overall nutritional quality of your daily diet?", 
        diet_options, index=diet_options.index(saved_diet)
    )

    c3, c4 = st.columns(2)
    alc_options = ["Never", "Rarely", "Weekly", "Daily"]
    saved_alc = st.session_state.ml_data.get("Alcohol_Frequency", "Never")
    st.session_state.ml_data["Alcohol_Frequency"] = c3.selectbox(
        "How often do you consume alcohol?", 
        alc_options, index=alc_options.index(saved_alc)
    )
    
    smoke_options = ["Never", "Former", "Current"]
    saved_smoke = st.session_state.ml_data.get("Smoking", "Never")
    st.session_state.ml_data["Smoking"] = c4.selectbox(
        "Are you a smoker/vaper?", 
        smoke_options, index=smoke_options.index(saved_smoke)
    )

    st.session_state.ml_data["Screen_Time_Hours_Day"] = st.slider(
        "Outside of work/study, how many hours per day do you spend on your phone or TV?", 
        0.0, 24.0, value=float(st.session_state.ml_data.get("Screen_Time_Hours_Day", 5.0))
    )
    st.session_state.ml_data["Hobby_Time_Hours_Week"] = st.slider(
        "How many hours a week do you spend specifically on hobbies?", 
        0.0, 50.0, value=float(st.session_state.ml_data.get("Hobby_Time_Hours_Week", 5.0))
    )

    st.write("")
    col1, col2 = st.columns(2)
    if col1.button("Back", use_container_width=True):
        st.session_state.page = "social_life"
        st.rerun()
        
    if col2.button("Submit", type="primary", use_container_width=True):

        if st.session_state.ml_data.get("Employment_Status") == "Unemployed":
            st.session_state.ml_data["Work_Hours_Per_Week"] = 0
            st.session_state.ml_data["Remote_Work"] = "No"
            st.session_state.ml_data["Job_Satisfaction"] = 0
            st.session_state.ml_data["Work_Stress_Level"] = 0
            st.session_state.ml_data["Work_Life_Balance"] = 10
            st.session_state.ml_data["Company_Mental_Health_Support"] = "No"
            
        income_mapping = {
            "Low (Often insufficient)": "Low", 
            "Medium (Adequate)": "Middle", 
            "High (Very sufficient)": "High"
        }
        st.session_state.ml_data["Income_Level"] = income_mapping[st.session_state.ml_data["Income_UI"]]
        
        discuss_mapping = {
            "Never (Keep it to myself)": "Never",
            "Rarely": "Rarely",
            "Sometimes": "Sometimes",
            "Very easily": "Yes easily",
        }
        st.session_state.ml_data["Discuss_Mental_Health"] = discuss_mapping[st.session_state.ml_data["Discuss_UI"]]
        
        st.session_state.page = "result"
        st.rerun()