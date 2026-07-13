
import streamlit as st
import pandas as pd
from sklearn.inspection import permutation_importance
from loader import X, y, model
import plotly.express as px

from utils import get_text

def app():
    cols = st.columns(2)
    perm_importance = permutation_importance(model, X, model.predict(X), n_repeats=5, random_state=42)

    perm_importance_df = pd.DataFrame({
        'Feature': X.columns,
        'Importance': perm_importance.importances_mean
    }).sort_values(by='Importance', ascending=False)

    perm_importance_df = perm_importance_df.sort_values(by='Importance', ascending=False)
    
    importance_str = get_text('perm_importance')
    fig = px.bar(perm_importance_df, y='Feature', x='Importance', orientation='h',
                labels={'Importance': importance_str, 'Feature': 'Feature'},
                title=importance_str)
    fig.update_layout(yaxis=dict(autorange='reversed'))
    cols[0].plotly_chart(fig)