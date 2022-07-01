import streamlit as st

from PIL import Image

st.set_page_config(page_title="Drum Corps International", layout="wide")

st.title("Drum Corps International")
st.markdown(
    """
    Welcome to my Drum Corps International (DCI) Analysis page.  Here you will find information on \
    DCI Score Predictions, Historical Scores (2013-2019), as well as Different Types of Analyses.
    
    You can find a graph of the current 2022 Scores to Date on the Historical Scores page and drilling down to 2022.
    
    Feel free to browse the site and let me know what you think.  Let us enjoy the 2022 Season Together!
    
    1. [Today's Predictions](#predictions)
    1. [Finals Predictions](#finals)
    1. [Past Predictions](#pastpredictions)
    """)

finals_pred_image = Image.open('images/finals_predictions.png')
corps_at_the_crest_image = Image.open('images/corps_at_the_crest_predictions.png')
drum_corps_at_the_rose_bowl_image = Image.open('images/drum_corps_at_the_rose_bowl_predictions.png')
western_corps_connection_image = Image.open('images/western_corps_connection_predictions.png')
tour_premiere_image = Image.open('images/tour_premiere_predictions.png')
central_indiana_image = Image.open('images/central_indiana_predictions.png')

col1, col2, col3 = st.columns([3, 3, 0.2])

col1.markdown('<a id="predictions"></a>', unsafe_allow_html=True)
col1.markdown("## Today's Predictions")

#col2.text(" ")
#col2.markdown("## Sunday Predictions")
col1.image(central_indiana_image, caption='2022 DCI Central Indiana Predictions, Muncie, IN')

col1.markdown('<a id="finals"></a>', unsafe_allow_html=True)
col1.markdown('## Finals Predictions')
col1.image(finals_pred_image, caption='2022 Finals Predictions, Indianpolis, IN')

col1.markdown('<a id="pastpredictions"></a>', unsafe_allow_html=True)
col1.markdown('## Past Predictions')

col1.image(tour_premiere_image, caption='2022 DCI Tour Premiere Predictions, Detroit, MI')
col1.image(western_corps_connection_image, caption='2022 Western Corps Connections Predictions, San Bernardino, CA')
col1.image(drum_corps_at_the_rose_bowl_image, caption='2022 Drum Corps at the Rose Bowl Predictions, Pasadena, CA')
col1.image(corps_at_the_crest_image, caption='2022 Corps at the Crest Predictions, Vista, CA')