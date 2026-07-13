import time
import streamlit as st
from loader import model, accuracy_result
from data.config import thresholds
from function.function import make_donut
from data.base import mrk
from utils import get_text


def app(input_data):
    prediction = model.predict_proba(input_data)[:, 1]

    cols = st.columns(2)

    def stream_data():
        is_diabetes = get_text('diabetes') if prediction >= thresholds else get_text('no_diabetes')
        text = f"{get_text('model_accuracy')}: {accuracy_result}%\n\n"
        for word in text.split(" "):
            yield word + " "
            time.sleep(0.05)
        text = f"\n{get_text('prediction_label')}: {is_diabetes}\n"
        for word in text.split(" "):
            yield word + " "
            time.sleep(0.05)
        text = f"\n{get_text('probability_label')}: {(prediction * 100).round(2)[0]}%\n"
        for word in text.split(" "):
            yield word + " "
            time.sleep(0.05)
        
        return 80

    cols[0].write_stream(stream_data)


    is_diabetes = get_text('warning_diabetes') if prediction >= thresholds else get_text('no_diabetes')
    color = f'red' if prediction >= thresholds else 'blue'

    cols[1].markdown(mrk.format(color, is_diabetes), unsafe_allow_html=True)
    cols[1].write('\n\n\n\n\n')
    donut_chart_population = make_donut((prediction * 100).round(2)[0], 
                                        get_text('diabetes_risk'),
                                        input_color=color)

    cols[1].altair_chart(donut_chart_population)