import streamlit as st 
st.title("Cloud PaaS Demo") 
st.write("Ứng dụng này được xây dựng bằng Python và Streamlit.") 
name = st.text_input("Nhập tên của bạn") 
if name: 
    st.write(f"Xin chào {name}!") 
st.subheader("Ý nghĩa cloud") 
st.write("Khi triển khai lên Streamlit Cloud, ứng dụng này sẽ chạy trên nền tảng PaaS.") 