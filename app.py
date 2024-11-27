import streamlit as st
import pandas as pd
from sklearn.datasets import load_wine

values, target = load_wine(return_X_y=True)
target_names = load_wine().target_names
feature_names = load_wine().feature_names

st.title('Bienvenue !')

df = pd.DataFrame(values, columns=feature_names)
df
plot = df['alcohol']

bot = st.checkbox("afficher le graphique de la colone alcohol")

if bot:
    st.line_chart(plot)
  
