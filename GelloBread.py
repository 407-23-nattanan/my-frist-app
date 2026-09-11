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

if st.button("คำนวนค่า BMI 🎯"):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

    st.write("---")
    st.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")

    if bmi < 18.5:
        st.warning("⚠️ คุรมีน้ำหนักน้อยกว่าเกณฑ์ (ผอม)")
    elif 18.5 <= bmi < 23.0:
        st.success("🎉 คุณมีน้ำหนักอยู่ในเกณฑ์ปกติ (สุขภาพดี)")
    elif 23.0 <= bmi < 25.0:
        st.info("💡 คุณมีน้ำหนักเกินกว่าเกณฑ์ (ท้วม)")
    else:
        st.error("🚨 คุณอยู่ในเกณฑ์อ้วน ควรระวังเรื่องสุขภาพและออกกำลังกาย")

