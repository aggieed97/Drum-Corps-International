import streamlit as st

from PIL import Image

st.set_page_config(page_title="Drum Corps International", layout="wide")

st.title("World Class Corps Score Predictions")

st.markdown("This page is under construction. It currently has pages for Historical Scores and Past DCI Champions. Future plans include adding some DCI Score Analysis as well as Performance predictions.")
st.markdown('For now, enjoy my 2022 DCI Finals Prediction for Competition that will take place in Indianapolis, IN on August 13, 2022.')
finals_pred_image = Image.open('images/finals_predictions.png')
corps_at_the_crest_image = Image.open('images/corps_at_the_crest_predictions.png')

col1, col2, col3 = st.columns([3, 5, 0.2])
col1.image(corps_at_the_crest_image, caption='2022 Corps at the Crest Predictions, Vista, CA')
col1.image(finals_pred_image, caption='2022 Finals Predictions, Indianpolis, IN')
