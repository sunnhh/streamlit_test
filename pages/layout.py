import streamlit as st

st.title("Layout")

col1, col2 = st.columns(2)

with col1:
    st.write("col1!!!")
with col2:
    st.write("col2!!!")

tab1, tab2 = st.tabs(['봄', '가을'])

with tab1:
    st.write("봄이에요!")
with tab2:
    st.write("가을이에요!")