import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import pickle

st.title("🚀 Resume Classifier")

# File upload
uploaded_file = st.file_uploader("Upload resume (txt/pdf)", type=['txt','pdf'])

if uploaded_file:
    # Read text (simplified)
    text = str(uploaded_file.read())
    st.text_area("Resume text:", text, height=200)
    
    # Dummy prediction (replace with actual model)
    categories = ['HR', 'Developer', 'Designer', 'Manager']
    prediction = np.random.choice(categories)
    st.success(f"🎯 Predicted Category: **{prediction}**")
