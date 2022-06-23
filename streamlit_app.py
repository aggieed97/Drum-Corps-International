import streamlit as st

from PIL import Image

st.set_page_config(page_title="Drum Corps International", layout="wide")

st.title("Drum Corps International")
st.markdown(
    """
    Welcome to my Drum Corps International (DCI) Analysis page.  Here you will find information on \
    DCI Score Predictions, Historical Scores (2013-2019), as well as Different Types of Analyses.
    
    Feel free to browse the site and let me know what you think.  Let us enjoy the 2022 Season Together!
    
    1. [Current Predictions](#predictions)
    1. [Finals Predictions](#finals)
    1. [Past Predictions](#pastpredictions)
    """)

finals_pred_image = Image.open('images/finals_predictions.png')
corps_at_the_crest_image = Image.open('images/corps_at_the_crest_predictions.png')

col1, col2, col3 = st.columns([3, 5, 0.2])

col1.markdown('<a id="predictions"></a>', unsafe_allow_html=True)
col1.markdown('## Predictions')
col1.image(corps_at_the_crest_image, caption='2022 Corps at the Crest Predictions, Vista, CA')

col1.markdown('<a id="finals"></a>', unsafe_allow_html=True)
col1.markdown('## Finals Predictions')
col1.image(finals_pred_image, caption='2022 Finals Predictions, Indianpolis, IN')

col1.markdown('<a id="pastpredictions"></a>', unsafe_allow_html=True)
col1.markdown('## Past Predictions')
