import streamlit as st
from data.base import head, st_style, footer
from utils import get_text


def app():
    st.markdown(st_style, 
            unsafe_allow_html=True)

    head_text = head.replace('{0}', get_text('app_title')).replace('{1}', get_text('app_subtitle'))
    st.markdown(head_text, unsafe_allow_html=True)