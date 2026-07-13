import streamlit as st
import pandas as pd
from loader import (accuracy_result, 
                    f1_result, 
                    recall_result, 
                    precision_result, 
                    roc_auc)
from function.function import make_donut
from utils import get_text

def app():
    st.markdown(f"### {get_text('model_performance')}")
    # Model score
    cols = st.columns(5)
    color = 'blue'

    # Accuracy Score
    cols[0].markdown(get_text('acc_desc'))
    cols[0].altair_chart(make_donut(accuracy_result, 
                                    get_text('accuracy'),
                                    input_color=color,
                                    R=140,
                                    innerRadius=40,
                                    cornerRadius=10))

    # F1 Score
    cols[1].markdown(get_text('f1_desc'))
    cols[1].altair_chart(make_donut(f1_result, 
                                    get_text('f1_score'),
                                    input_color=color,
                                    R=140,
                                    innerRadius=40,
                                    cornerRadius=10))

    # Recall Score
    cols[2].markdown(get_text('recall_desc'))
    cols[2].altair_chart(make_donut(recall_result, 
                                    get_text('recall'),
                                    input_color=color,
                                    R=140,
                                    innerRadius=40,
                                    cornerRadius=10))

    # Precision Score
    cols[3].markdown(get_text('prec_desc'))
    cols[3].altair_chart(make_donut(precision_result, 
                                    get_text('precision'),
                                    input_color=color,
                                    R=140,
                                    innerRadius=40,
                                    cornerRadius=10))

    # ROC AUC Score
    cols[4].markdown(get_text('roc_desc'))
    cols[4].altair_chart(make_donut(roc_auc,
                                    get_text('roc_auc'),
                                    input_color=color,
                                    R=140,
                                    innerRadius=40,
                                    cornerRadius=10))
