import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from joblib import load
from joblib import dump


lr = LinearRegression()
loaded_lr = load("p3.linear.regression.model.joblib")
reg_tree = load("p3_dec_tree_model.joblib")

col1, col2 = st.columns([2,1])
col1.title("General Assembly Project 3")
col2.image("WOW_Real_Estate_Logo.png")
st.header("Predictive Pricing Model")
st.header("HDB Resale Market")
st.subheader("Abdallah (Bob) El Gohary, Ern-Min Peck, Ma Emily Sy",divider=True)
st.subheader("",divider=True)

col3, col4 = st.columns([2,1])
col3.subheader("Tell Me Your Dream Home")
# col4.selectbox(
#     "Predictive Model Preference",
#     ("Linear Regression","Decision Tree"),
#     index=0  # sets the default value to the first option
# )

col5, col6 = st.columns([2,1])
col5.subheader("Predicted Price:")


    # Updated list of keys including Serangoon (32 elements)
keys = [
    "Ang Mo Kio", "Bedok", "Bishan", "Bukit Batok", "Bukit Merah", 
    "Bukit Panjang", "Bukit Timah", "Changi", "Choa Chu Kang", "Clementi", 
    "Downtown core", "Geylang", "Hougang", "Jurong East", "Jurong West", 
    "Kallang", "Marine Parade", "Novena", "Outram", "Pasir Ris", 
    "Punggol", "Queenstown", "Rochor", "Sembawang", "Sengkang", 
    "Serangoon", "Tampines", "Tanglin", "Toa Payoh", "Westland Water Catchment", 
    "Woodlands", "Yishun"
]

# Dynamic dictionary comprehension
num_keys = len(keys)
planning_area_dict = {
    key: [1 if i == idx else 0 for i in range(num_keys)] 
    for idx, key in enumerate(keys)
}

room_keys = [
    "1 Room", "2 Room", "3 Room", "4 Room", "5 Room", 
    "Executive", "Multigeneration"
]

# Dynamic dictionary comprehension
num_room_keys = len(room_keys)
room_type_dict = {
    key: [1 if i == idx else 0 for i in range(num_room_keys)] 
    for idx, key in enumerate(room_keys)
}

with st.form("Home Price Prediction"):
    model = col4.selectbox(
        "Predictive Model Preference",
        ("Linear Regression","Decision Tree"),
        index=0  # sets the default value to the first option
        )
    
    flat_type = st.selectbox(
        "Enter Flat Type",
        ("1 Room","2 Room","3 Room","4 Room","5 Room","Executive","Multigeneration"),
        index=0  # sets the default value to the first option
    )

    planning_area = st.selectbox(
        "Enter Planning Area",
        ("Ang Mo Kio", "Bedok","Bishan","Bukit Batok", "Bukit Merah", "Bukit Panjang","Bukit Timah", "Changi", "Choa Chu Kang", "Clementi", "Downtown core",
        "Geylang", "Hougang", "Jurong East", "Jurong West", "Kallang", "Marine Parade", "Novena","Outram","Pasir Ris", "Punggol", "Queenstown", "Rochor",
        "Sembawang","Sengkang", "Serangoon", "Tampines", "Tanglin", "Toa Payoh", "Westland Water Catchment", "Woodlands", "Yishun"),
        index=0  # sets the default value to the first option
    )

    floor_mid = st.number_input("Enter Desired Floor",0,100)
    lease_age = st.number_input("Enter Lease Age",0,100)
    dist_mrt = st.number_input("Enter Distance to Nearest MRT in Meters",0,4000)
    dist_bus = st.number_input("Enter Distance to Nearest Bus Stop in Meters",0,500)
    dist_pri = st.number_input("Enter Distance to Nearest Primary School in Meters",0,3500)

    submit = st.form_submit_button("Confirm Preferences")

    if submit:
        pref_list = [floor_mid,lease_age,dist_mrt,dist_bus,dist_pri]
        
        features = pref_list + planning_area_dict[planning_area] + room_type_dict[flat_type]
        b = len(features)
        col6.subheader(f"{features}")
        # col6.subheader(f"1: {len(pref_list)}, 2: {len(planning_area_dict[planning_area])}, 3:{len(room_type_dict[flat_type])} ")
        if model == 'Linear Regression':
            col6.subheader(f"${round(loaded_lr.predict([features])[0], 2)}")
        else:
            col6.subheader(f"${round(reg_tree.predict([features])[0],2)}")





