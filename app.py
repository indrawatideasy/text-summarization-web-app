pip install torch
pip install tensorflow

import streamlit as st
from transformers import pipeline

# Load the summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Streamlit app
st.title("Text Summarization Web App")

# Input text box for the user
text = st.text_area("Enter text for summarization:", height=200)

# Optional parameters for summary length
max_length = st.slider("Maximum length of summary:", 50, 300, 130)
min_length = st.slider("Minimum length of summary:", 20, 100, 30)

# Summarize button
if st.button("Summarize"):
    if text:
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        st.subheader("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.write("Please enter text to summarize.")
