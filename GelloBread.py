import streamlit as st

st.title("GelloBread🥐")
st.divider() 

st.header("Order Summary")
A = st.number_input("ครัวซองค์ 45บาท/piece", min_value=0, value=0, step=1)
B = st.number_input("เจลาโต้รสพิสตาชีโอ 99บาท/serve", min_value=0, value=0, step=1)
C = st.number_input("ชิโอะปัง 55บาท/piece", min_value=0, value=0, step=1)

st.header("Payment Summary")
total = (A * 45) + (B * 99) + (C * 55)

# คำนวณเปอร์เซ็นต์ส่วนลด
discount_percent = 0

# ตรวจสอบส่วนลดตามยอดซื้อ
if total >= 500:
    discount_percent = 20
elif total > 199:
    discount_percent = 10

# ตรวจสอบว่าได้ส่วนลดจับคู่ครัวซองค์ + เจลาโต้ 5% หรือไม่
if A > 0 and B > 0:
    # เลือกเปอร์เซ็นต์ส่วนลดที่สูงที่สุด
    discount_percent = max(discount_percent, 5)

# คำนวณจำนวนเงินส่วนลดและราคาสุทธิ
discount_amount = total * (discount_percent / 100)
final_price = total - discount_amount

# แสดงผลใน Streamlit
st.subheader(f"ราคารวมทั้งหมด: {total:,.2f} บาท")
st.subheader(f"ส่วนลด ({discount_percent}%): -{discount_amount:,.2f} บาท")
st.subheader(f"ราคาหลังหักส่วนลด: {final_price:,.2f} บาท")
