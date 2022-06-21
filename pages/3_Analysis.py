import streamlit as st

from PIL import Image

st.set_page_config(page_title="DCI Analysis", layout="wide")

st.title("World Class Corps Analysis")

average_score_change = Image.open('images/score_change.png')

col1, col2 = st.columns([5, 5])
col1.image(average_score_change, caption='Performance Score Change 2013-2019')
col2.markdown('This graph shows the average score change for all Corps by performance throughout the years. \
 For example: if you look at the overall average of a step change in individual performance of 0.9011, \
 that means you can expect a Corps score to go up by that same amount for the next performance.')
col2.markdown('If Corps A scores a 70.000 on June 24, then you can expect their score to be approximately 70.901 \
 for the next performance.')
col2.markdown('However, you can see that there was a significant step change between average scoring changes from \
 2013-2015 and 2017-2019 with 2016 being quite the outlier.')
col2.markdown('I suspect a scoring rules change around 2016 and maybe yet another rules change that caused a step \
 back down from 2017 to 2019.  More research would need to be done to confirm that hypothesis.')
col2.markdown('Considering the average score change has been relatively flat from 2017-2019, we can use that expected \
 value of 0.9171 to help us determine how the Corps scores are improving throughout the 2022 season relative to that \
 value.')
