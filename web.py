import streamlit as st
from sentiments import sentiment_analyzer_scores
import time
from word_cloud import generate_wordcloud

st.title('Sentiment Analysis')
st.header('Senti-Tweet')
st.text("Emotion AI. What was the twitter user feeling?")

with st.spinner('Firing up the engines...'):
    time.sleep(2) # animate loading spinner

st.subheader('Single Sentence classification')
text_input = st.text_input('Sentence:')

# Make predictions
with st.spinner('Predicting...'):
    score = sentiment_analyzer_scores(text_input)

    # Show predictions
    if text_input != '':
        st.write('Prediction:')
        st.write(f'Neutral score: {score["neu"]}')
        st.write(f'Negative score: {score["neg"]}')
        st.write(f'Positive score: {score["pos"]}')
        st.write(f'Compound score: {score["compound"]}')

        if st.checkbox("Generate word cloud for phrase/Tweet"):
            generate_wordcloud(text_input, 'Tweet')



