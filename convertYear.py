import streamlit as st
st.title("แอปพลิเคชั่นแปลงปี พ.ศ. เป็น ค.ศ.")

bh__year=st.number_input("กรอกปี พ.ศ. ที่ต้องเปลี่ยนแปลง",value=2569)
ce__year=bh_year-543
st.header(f"ปี ค.ศ. คือ : {ce__year}")
