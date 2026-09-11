import streamlit as st

st.title("GelloBread🥐")
st.divider() 

st.header("Order Summary")
A = st.number_input("ครัวซองค์  45บาท/piece",min_value=0, value=0, step=1)
