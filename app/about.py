import streamlit as st
from utils import get_text

def app():
    st.markdown(get_text('about_diabetes_md'))
