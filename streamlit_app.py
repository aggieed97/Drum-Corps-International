import streamlit as st

from PIL import Image

st.set_page_config(page_title="Drum Corps International", layout="wide")

st.title("Today's Predictions")

image = Image.open('images/finals_predictions.png')

col1, col2, col3 = st.columns([3, 5, 0.2])
col2.image(image, caption='2022 Finals Predictions')
