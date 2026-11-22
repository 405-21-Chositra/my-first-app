import streamlit as st
st.title("🧾แอปคำนวณส่วนลดและ VAT 7%")
fullprice = st.number_input("กรอกราคาเต็มของสินค้า (บาท):", min_value=0.0 , value=0.0)
discount = st.number_input("กรอกส่วนลด (%):", min_value=0.0 , max_value=100.0 , value=0.0)
discount_price = fullprice * discount/100
discount = fullprice - discount_price
vat = discount * 0.07
net_price = fullprice - discount_price + vat
st.divider()#เส้นคั่นแบ่งสัดส่วนให้สวยงาม
st.header(f"● ส่วนลด ({discount}%): -{discount_price:.2f} บาท")
st.header(f"● ราคาหลังหักส่วนลด ({discount}%): -{discount_price:.2f = } บาท")
st.header(f"● ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")

st.header(f"● ราคาสุทธิ : {net_price:.2f} บาท")
st.divider()#เส้นคั่นแบ่งสัดส่วนให้สวยงาม
st.write("นางสาวโชศิตรา ดีวงค์ เลขที่ 21 ม.4/5")
