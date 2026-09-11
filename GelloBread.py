import streamlit as st

st.title("GelloBread🥐")
st.divider() 

st.header("Order Summary")
A = st.number_input("ครัวซองค์  45บาท/piece",min_value=0, value=0, step=1)
B = st.number_input("เจลาโต้รสพิสตาชีโอ 99บาท/serve",min_value=0, value=0, step=1)
C = st.number_input(" ชิโอะปัง  55บาท/piece",min_value=0, value=0, step=1)

st.header("Payment Summary")
total = (A * 45) + (B * 99) + (C * 55)
st.subheader(f"ราคารวมทั้งหมด: {total:,} บาท")
