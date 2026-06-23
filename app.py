import streamlit as st
from utils.pdf_reader import read_pdf
from utils.llm import ask_gemini

st.title("AI Document Assistant")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file is not None:
    text = read_pdf(uploaded_file)

    st.success("Đã đọc PDF thành công")

    with st.expander("Xem nội dung PDF"):
        st.write(text[:3000])

    question = st.text_input("Nhập câu hỏi về tài liệu")

    if question:
        answer = ask_gemini(text[:12000], question)
        st.write(answer)