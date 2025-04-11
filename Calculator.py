import streamlit as st
st.title("A simple Calculator")
first_numb=st.number_input("Enter your first number",value=None)
second_numb=st.number_input("Enter second number",value=None)
sign=st.selectbox("Choose operation",["+","-","/","*"])
if st.button("Calculate"):
    if sign == "+":
        result=first_numb+second_numb
        st.success(f"Result={result}")
    elif sign == "-" :
        result=(first_numb - second_numb)
        st.success(f"Result = {result}")
    elif sign == "/" :
        result =(first_numb / second_numb)
        st.success(f"Result = {result}")
    elif sign == "*":
        result = (first_numb * second_numb)
        st.success(f"Result = {result}")    
