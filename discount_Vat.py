import streamlit as st
st.title("🧾แอปคำนวณส่วนลดราคาและ VAT 7%")
price = st.number_input("กรอกราคาสินค้า (บาท):", min_value=0.0 , value=0.0)
