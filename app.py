# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 16:19:25 2024

@author: prachet
"""

import streamlit as st
import joblib
from pathlib import Path

#set the page title
st.set_page_config(page_title="Sentiment Analysis App",page_icon="😃")

#App title and description

st.title("Sentiment Analysis App")
st.write("This app predicts the sentiment of text based on different sources")

#define the path of models
models_dir = Path('models')

#check if model dir exists
if not models_dir.exists():
    st.error(f"Models directory not found at {models_dir.resolve()}. Please ensure the ")
    st.stop()
    
#load available sources
try:
    sources = [file.stem.split('_')[1] for file in models_dir.glob('model_*.joblib')]

    if not sources:
        st.error("No models found in the models directory. Please add model files with")
        st.stop()
except Exception as e:
    st.error(f"Error loading models: {e}")
    st.stop()

#user input

selected_source = st.selectbox("Select a source", sources)
user_text = st.text_area("Enter your text here:")


def load_model_and_vectorizer(source):
    try:
        #load the trained model
        model_path = f'models/model_{source}.joblib'
        vectorizer_path = f'models/vectorizer_{source}.joblib'
        model = joblib.load(model_path)
        vectorizer = joblib.load(vectorizer_path)
        return model , vectorizer
    except Exception as e:
        st.error(f"Error loading model or vectorizer: {e}")
        return None , None
    
def predict_sentiment(text , source):
    model , vectorizer = load_model_and_vectorizer(source)
    if model is None or vectorizer is None:
        return "Error"
    try:
        #transform the input text to numeric format using vectorizer
        transformed_text = vectorizer.transform([text])
        
        #make the prediction using tarnsformed text
        prediction = model.predict(transformed_text)[0]
        return prediction
    except Exception as e:
        st.error(f"Error during prediction : {e}")
        return "Error"

if st.button("Predict Sentiment"):
    if user_text.strip():
        #perform sentiment prediction
        sentiment = predict_sentiment(user_text, selected_source)
        
        #Display Result
        st.subheader("Prediction Results:")
        if sentiment == "Positive":
            st.success(f"The sentiment is {sentiment} 😃")
        elif sentiment == "Negative":
            st.error(f"The sentiment is {sentiment} 😞")
        elif sentiment == "Neutral":
            st.info(f"The sentiment is {sentiment} 🙂")
        else:
            st.warning(f"Received unexpected sentiment: {sentiment}")
    else:
        st.warning("Please enter some text for prediction")

















