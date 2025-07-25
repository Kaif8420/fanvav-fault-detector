import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os

from feature_engineer import FeatureEngineer 

st.set_page_config(layout="wide")

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

@st.cache_resource
def load_model(path):
    return joblib.load(path)

data_path = os.path.join("..", "data", "combined_pfpu_data.csv")
model_path = os.path.join("..", "models", "random_forest_model.pkl")

df = load_data(data_path)
model = load_model(model_path)

st.title("🔥 PFPU Fault Detection Dashboard")
st.write("### Sample Data", df.head())

# Fault Type Distribution
st.write("### Fault Type Distribution")
fig2, ax2 = plt.subplots()
sns.countplot(data=df, x='fault_type', ax=ax2)
st.pyplot(fig2)

# Feature Engineering
fe = FeatureEngineer(df)
X, y = fe.preprocess()

# Feature Importances from Processed Features
st.write("### Top Feature Importances")
importances = model.feature_importances_
features = X.columns

top_features = pd.DataFrame({'Feature': features, 'Importance': importances})
top_features = top_features.sort_values('Importance', ascending=False).head(10)

fig, ax = plt.subplots()
sns.barplot(data=top_features, x='Importance', y='Feature', ax=ax)
st.pyplot(fig)
