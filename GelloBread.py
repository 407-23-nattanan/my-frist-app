import streamlit as st

st.title("GelloBread🥐")
st.divider() 

st.header("Order Summary")
A = st.number_input("ครัวซองค์ 45บาท/piece", min_value=0, value=0, step=1)
B = st.number_input("เจลาโต้รสพิสตาชีโอ 99บาท/serve", min_value=0, value=0, step=1)
C = st.number_input("ชิโอะปัง 55บาท/piece", min_value=0, value=0, step=1)
st.divider() 

st.header("Payment Summary")
total = (A * 45) + (B * 99) + (C * 55)

discount_percent = 0

if total >= 500:
    discount_percent = 20
elif total > 199:
    discount_percent = 10

if A > 0 and B > 0:
    discount_percent = max(discount_percent, 5)

discount_amount = total * (discount_percent / 100)
Net_Total = total - discount_amount

st.subheader(f"ราคารวมทั้งหมด: {total:,.2f} บาท")
st.subheader(f"ส่วนลด ({discount_percent}%): -{discount_amount:,.2f} บาท")
st.subheader(f"ราคาหลังหักส่วนลด: {Net_Total:,.2f} บาท")
st.divider() 

st.header("Cash Payment")
X = st.number_input("รับเงิน -บาท", min_value=0, value=0, step=5)
if Net_Total > 0:
    if X >= Net_Total:
        change = X - Net_Total
        st.subheader(f"เงินทอน: {change:,.2f} บาท")
    else:
        st.warning(f"ยังขาดอีก {Net_Total - X:,.2f} บาท")
else:
    st.subheader("เงินทอน: 0.00 บาท")
