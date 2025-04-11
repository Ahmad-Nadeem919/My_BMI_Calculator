import streamlit as st
import pandas as pd
st.title("BMI calculator")
height=st.slider("Enter your height in cm",100,250,175)
weight=st.slider("Enter your weight in kg",50,100,70)
if st.button("Calculate BMI"):
    height_m = height / 100

# Correct BMI formula
    bmi1 = weight / (height_m ** 2)
    bmi=f"{bmi1:.2f}"
    bmi=float(bmi)
    st.write(f"Your BMI weight is {bmi}")
    if bmi < 18.00:
        st.info("you are underweight")
    elif 18.00<= bmi <= 24.00:
        st.success("you have normal weight ") 
    elif 25.00 <= bmi >=29.00:
        st.success("you are over weight")
    else :
        st.error("un suitable weight")
                    
