import streamlit as st
from joblib import load

language_list = ['english', 'chinese', 'french', 'spanish', 'italian', 'german', 'korean', 'japanese']
language_list_caps = []
pro_models = {}
tutor_models = {}
for language in language_list:
    language_list_caps.append(language.capitalize())
    language_tutor_str = f'{language}_tutor.joblib'
    language_pro_str = f'{language}_tutor.joblib'
    pro_models[language] = load(language_pro_str)
    tutor_models[language] = load(language_tutor_str)

loaded_lr = load("p3.linear.regression.model.joblib")
reg_tree = load("p3_dec_tree_model.joblib")

col1, col2 = st.columns([2,1])
col1.title("General Assembly Project 4")
col2.image("italki_logo.png")
st.header("Are your fees right?")
st.subheader("",divider=True)

col3, col4 = st.columns([2,1])
col3.subheader("Let's see how we can do better")
# col4.selectbox(
#     "Predictive Model Preference",
#     ("Linear Regression","Decision Tree"),
#     index=0  # sets the default value to the first option
# )

col5, col6 = st.columns([2,1])
col5.subheader("Predicted Price:")

with st.form("What is my Price?"):
    pro_or_tutor = col4.selectbox(
        "Are you a professional teacher or a tutor?",
        ("Professional","Tutor"),
        index=0  # sets the default value to the first option
        )

    # floor_mid = st.number_input("Enter Desired Floor",0,100)
    # lease_age = st.number_input("Enter Lease Age",0,100)
    # dist_mrt = st.number_input("Enter Distance to Nearest MRT in Meters",0,4000)
    # dist_bus = st.number_input("Enter Distance to Nearest Bus Stop in Meters",0,500)
    # dist_pri = st.number_input("Enter Distance to Nearest Primary School in Meters",0,3500)


    language_taught = st.selectbox("What language do you teach?", language_list_caps)
    language_taught = language_taught.lower()
    trial_sessions = st.number_input("How many trial sessions have you completed?",0,10000)
    trial_price = st.number_input("What is your current trial price (USD)?",5,120)
    has_package = st.radio("Do you offer packages?", ("Yes", "No"))
    student_count = st.number_input("How many students have you taught?",1,3000)
    session_count = st.number_input("How many sessions have you conducted?",1,15000)

    submit = st.form_submit_button("Confirm Preferences")

    # if submit:
        # pref_list = [floor_mid,lease_age,dist_mrt,dist_bus,dist_pri]
        
        # features = pref_list
        # # b = len(features)
        # # col6.subheader(f"{features}")
        # # col6.subheader(f"1: {len(pref_list)}, 2: {len(planning_area_dict[planning_area])}, 3:{len(room_type_dict[flat_type])} ")
        # if pro_or_tutor == 'Professional':
        #     col6.subheader(f"${round(loaded_lr.predict([features])[0], 2)}")
        # else:
        #     col6.subheader(f"${round(reg_tree.predict([features])[0],2)}")

    if has_package == 'Yes':
        has_package = 1
    else:
        has_package = 0

    if submit and session_count >= student_count:
        trial_price_cents = round(trial_price/100, 2)
        session_to_student = session_count/student_count
        features_list = [trial_sessions, trial_price_cents, has_package, session_to_student]
        
        if pro_or_tutor == 'Professional':
            pred_price = round(pro_models[language_taught].predict([features_list])[0] / 100, 2)
            col6.subheader(f"US${pred_price}")
            col6.markdown(f"###### Your profit is US${round(pred_price * 0.79, 2)} per session")
            # col6.subheader(f"{pro_or_tutor}, {pro_models}, {language_taught}")
        else:
            pred_price = round(tutor_models[language_taught].predict([features_list])[0] / 100, 2)
            col6.subheader(f"US${pred_price}")
            col6.markdown(f"###### Your profit is US${round(pred_price * 0.79, 2)} per session")
            # col6.subheader(f"{pro_or_tutor}, {tutor_models[language_taught]}, {language_taught}")
    elif submit:
        col6.markdown("##### The number of students cannot be more than the sessions conducted")

        
        





