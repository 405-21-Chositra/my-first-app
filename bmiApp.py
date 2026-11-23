import streamlit as st









if st.button("คำนวณค่า BMI 🎯"):
  # แปลงส่วนสูงจาก cm เป็น เมตร แล้วคำนวณ BMI
  height_m = height_cm / 100
  bmi = weight / (height_m ** 2)


st.write("---")
st.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}")
