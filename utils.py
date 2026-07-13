import streamlit as st
from locales import translations

def get_text(key):
    lang = st.session_state.get('lang', 'English')
    if lang not in translations:
        lang = 'English'
    return translations[lang].get(key, translations['English'].get(key, key))
