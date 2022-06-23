import streamlit as st
import pandas as pd

from PIL import Image

st.set_page_config(page_title="DCI Analysis", layout="wide")

st.title("World Class Corps Analysis")
st.markdown(
    """
    Here you will find different types of analyses throughout the 2022 DCI Summer Tour.
    
    Feel free to reach out at anytime if you would like to discuss my findings and conclusions.

    1. [Naive Predictions Using Past Average Score Change (All World Class Corps)](#allavgscorechange)
    1. [Naive Predictions Using Past Average Score Change for Each Individual Corps](#indavgscorechange)
    """)

average_score_change = Image.open('images/score_change.png')
actual_vs_expected = Image.open('images/actual_vs_expected.png')

st.markdown('<a id="allavgscorechange"></a>', unsafe_allow_html=True)
st.markdown('### Average Score Change (All World Class Corps)')

col1, col2 = st.columns([5, 5])

col1.image(average_score_change, caption='Performance Score Change 2013-2019')
col2.markdown(
    """
 This graph shows the average score change for all Corps by performance throughout the years. \
 For example: if you look at the overall average of a step change in individual performance of 0.9011, \
 that means you can expect a Corps score to go up by that same amount for the next performance.
 
 If Corps A scores a 70.000 on June 24, then you can expect their score to be approximately 70.901 \
 for the next performance.
 
 However, you can see that there was a significant step change between average scoring changes from \
 2013-2015 and 2017-2019 with 2016 being quite the outlier.
 
 I suspect a scoring rules change around 2016 and maybe yet another rules change that caused a step \
 back down from 2017 to 2019.  More research would need to be done to confirm that hypothesis.
 
 Considering the average score change has been relatively flat from 2017-2019, we can use that expected \
 value of 0.9171 to help us determine how the Corps scores are improving throughout the 2022 season relative to that \
 value.
 
 In theory.  Upon further thought, it may be better to determine the expected score on each individual Corps average \
 performance score change rather than an average of all 22 Corps.
 """)

st.markdown('<a id="indavgscorechange"></a>', unsafe_allow_html=True)
st.markdown('### Average Score Change (Individual Corps)')

score_change_mean_dict = {'Blue Devils': 1.12,
                         'Blue Knights': 1.01,
                         'Blue Stars': 0.98,
                         'Bluecoats': 0.95,
                         'Boston Crusaders': 0.96,
                         'Carolina Crown': 0.96,
                         'Colts': 0.95,
                         'Crossmen': 0.95,
                         'Genesis': 0.96,
                         'Jersey Surf': 0.94,
                         'Madison Scouts': 0.93,
                         'Mandarins': 0.94,
                         'Music City': 0.95,
                         'Pacific Crest': 0.95,
                         'Phantom Regiment': 0.94,
                         'Santa Clara Vanguard': 0.95,
                         'Seattle Cascades': 0.93,
                         'Spirit of Atlanta': 0.93,
                         'The Academy': 0.92,
                         'The Cadets': 0.92,
                         'The Cavaliers': 0.92,
                         'Troopers': 0.92
                         }

score_change_df = pd.DataFrame.from_dict(score_change_mean_dict, orient='index',
                columns = ['Average Score Change']).reset_index().rename(columns={'index':'Drum Corps'})

final_score_change_df = score_change_df.style.set_caption('Average Score Change by Corps (2017-2020)').hide_index() \
    .format({'Average Score Change':'{:.3}'}) \
    .set_table_styles([dict(selector='th', props=[('text-align', 'center')])]) \
    .set_table_styles([{'selector': 'th.col_heading', 'props': 'text-align: center;'}], overwrite=False)

col3, col4 = st.columns([3, 5])
col3.write(final_score_change_df.to_html(), unsafe_allow_html=True)

col4.markdown(
    """
    In the table on the left, we have the average score change by performance for each Individual World Class Corps \
    from 2017-2019.  We use those dates to reflect what we saw above with the step change between 2013-2015 and \
    2017-2019.
    
    Using this information, once we know each Corps beginning score, we can project out the total scores \
    with a naive approach by adding these averages to the previous final score.
    
    For example, if the Blue Devils score a 70.0 on their first performance on Saturday, June 25th, \
    we can then predict that they will score a 71.12 on their 2nd performance on Sunday, June 26th.
    
    These calculated values can then be use as "expected" scores that we can compare against the actual scores.
    
    This will give us an idea of how the Corps are performing relative to how they've performed in the past.
    
    From the figure below with the approach above, you can see that the Bluecoats scored better than expected \
    throughout nearly all of the 2019 Season, but then fell below expectation the last week beginning in Allentown, PA \
    and running through Championship Weekend.
    """
)

col4.image(actual_vs_expected, caption='Blue Coats Performance Evaluation for 2019')
