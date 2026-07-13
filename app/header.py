import streamlit as st
from data.base import head, st_style, footer
from utils import get_text


def app():
    st.markdown(st_style, 
            unsafe_allow_html=True)

    st.markdown(footer.format(get_text('footer_text'), get_text('github')), 
                unsafe_allow_html=True)


    st.markdown(head.format(get_text('app_title'), get_text('app_subtitle')), 
        unsafe_allow_html=True
    )