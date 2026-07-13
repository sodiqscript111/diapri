import streamlit as st
import shap
import time
from loader import model
import matplotlib.pyplot as plt
from utils import get_text


def app(input_data):
    sample_transformed = model.named_steps['feature_engineering'].transform(input_data)
    explainer = shap.TreeExplainer(model.named_steps['model'])
    shap_values_single = explainer.shap_values(sample_transformed)

    shap_values_class_1 = shap_values_single[0][:, 1]  


    def stream_data():
        text = f"""
{get_text('your_inputs')}\n
`Pregnancies`: {float(input_data.iloc[0]['Pregnancies'])}\n
`Glucose`: {float(input_data.iloc[0]['Glucose'])}\n
`Insulin`: {float(input_data.iloc[0]['Insulin'])}\n
`BMI`: {float(input_data.iloc[0]['BMI'])}\n
`Age`: {float(input_data.iloc[0]['Age'])}
                """
        for word in text.split(" "):
            yield word + " "
            time.sleep(0.05)

    # Layout with two columns
    cols = st.columns(2)

    # Column 1: Stream user input
    with cols[0]:
        st.markdown(f"### {get_text('input_streaming')}")
        st.markdown(f"#### {get_text('see_inputs_realtime')}")
        for word in stream_data():
            st.write(word)

    # SHAP Waterfall Plot
    fig, ax = plt.subplots()
    shap.plots.waterfall(
        shap.Explanation(
            values=shap_values_class_1,
            base_values=explainer.expected_value[0],
            data=sample_transformed.iloc[0],
            feature_names=sample_transformed.columns.tolist()
        ), show=False
    )
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    # Column 2: SHAP Waterfall Plot
    with cols[1]:
        st.markdown(f"### {get_text('shap_waterfall_plot')}")
        st.markdown(get_text('shap_waterfall_md'))
        st.pyplot(fig)

    # SHAP Force Plot
    force_plot_html = shap.force_plot(
        base_value=explainer.expected_value[1],
        shap_values=shap_values_single[0][:, 1],
        features=sample_transformed.iloc[0],
        feature_names=sample_transformed.columns.tolist()
    )

    # Explanation column
    st.markdown(
        f"### {get_text('column_explanations')}\n" + get_text('column_explanations_md') + "\n\n\n\n",
        unsafe_allow_html=True,
    )

    force_plot_html = f"<head>{shap.getjs()}</head><body>{force_plot_html.html()}</body>"
    st.markdown(f"### {get_text('shap_force_plot')}")
    st.components.v1.html(force_plot_html, height=400)