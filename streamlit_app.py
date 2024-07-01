import streamlit as st
import pandas as pd
import plotly.express as px

from PIL import Image

st.set_page_config(page_title="Drum Corps International", layout="wide")

st.title("Drum Corps International")
st.markdown(
    """
    Welcome to my Drum Corps International (DCI) Analysis page.  Here you will find information on \
    DCI Score Predictions, Historical Scores (2013-2019), as well as Different Types of Analyses.
    
    Feel free to browse the site and let me know what you think.  Let us enjoy the 2022 Season Together!
    
    1. [2022 Analysis](#analysis)
    1. [Today's Predictions](#today)
    1. [Max Rank by Score](#max_rank)
    1. [Pre-Season Finals Predictions](#finals)
    1. [Past Predictions](#pastpredictions)
    """)

max_rank_image = Image.open('images/rank_by_max_score.png')
finals_pred_image = Image.open('images/finals_predictions.png')
corps_at_the_crest_image = Image.open('images/corps_at_the_crest_predictions.png')
drum_corps_at_the_rose_bowl_image = Image.open('images/drum_corps_at_the_rose_bowl_predictions.png')
western_corps_connection_image = Image.open('images/western_corps_connection_predictions.png')
tour_premiere_image = Image.open('images/tour_premiere_predictions.png')
central_indiana_image = Image.open('images/central_indiana_predictions.png')
dci_austin = Image.open('images/austin_predictions.png')
dci_denton = Image.open('images/denton_predictions.png')
dci_houston = Image.open('images/houston_predictions.png')
dci_prelims = Image.open('images/prelims_predictions.png')
dci_semis = Image.open('images/semis_predictions.png')
dci_finals = Image.open('images/finals_predictions.png')

df = pd.read_csv('pages/2024-World-Class-DCI-scores.csv')
dci_colors = pd.read_csv('pages/drum_corps_colors.csv')
color_discrete_map = dict(dci_colors.values)

first_place_finishes = df.query("Rank == '1st'").Corps.value_counts().reset_index().rename(columns={"index":"Drum Corps", "Corps":"1st Place Finish"})

df['Date'] = pd.to_datetime(df.Date)
df['Year'] = df.Date.dt.year
score_df = df.sort_values(by=['Corps', 'Date']).reset_index(drop=True)
corps = list(score_df.Corps.unique())
corps.insert(0, "All")


col1, col2, col3 = st.columns([5, 3, 0.2])

col1.markdown('<a id="analysis"></a>', unsafe_allow_html=True)
col1.markdown("## 2024 Analysis")

corp = st.selectbox('Choose a Drum Corps:', corps)

if corp == 'All':
    filtered_df = score_df.copy()
    height = 900
    annotation_xtext = 0.85
    annotation_ytext = -0.10
else:
    filtered_df = score_df[(score_df.Corps == corp)].reset_index(drop=True)
    height = 500
    annotation_xtext = 0.85
    annotation_ytext = -0.20

fig2 = px.line(
    data_frame=filtered_df,
    x='Date',
    y='Score',
    color='Corps',
    color_discrete_map=color_discrete_map,
    markers=True,
    hover_name='Location',
    template='seaborn'
).update_layout(
    autosize=False,
    width=500,
    height=height,
    title=f'{corp} Scores for 2024',
    font=dict(
        size=20
    )
).add_annotation(dict(font=dict(size=15),
                      x=annotation_xtext,
                      y=annotation_ytext,
                      showarrow=False,
                      text="Data: https://dci.org<br>Graphic: @Danger009Mouse",
                      textangle=0,
                      xanchor='left',
                      xref="paper",
                      yref="paper")
                 )

st.plotly_chart(fig2, use_container_width=True)

fig1 = px.bar(
    data_frame=first_place_finishes,
    x="1st Place Finish",
    y='Drum Corps',
    color='Drum Corps',
    color_discrete_map=color_discrete_map,
).update_layout(
    title={
        'text': 'Drum Corps International <br># of 1st Place Finishes by Corps to Date',
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title='1st Place Rank Count',
    yaxis_title='Drum Corps',
    font=dict(
        size=15,
    ),
    width=250,
    height=500,
    showlegend=False,
    margin=dict(
        l=25,
        r=25,
        b=100,
        t=100,
        pad=4
    ),
    xaxis = dict(
        tickmode='linear',
        tick0=0,
        dtick=1
    )
).add_annotation(dict(font=dict(color='white', size=15),
                                                       x=0.8,
                                                       y=-0.3,
                                                       showarrow=False,
                                                       text="Data: https://www.dci.org<br>Graphic: @Danger009Mouse",
                                                       textangle=0,
                                                       xanchor='left',
                                                       xref="paper",
                                                       yref="paper")
                                                  )
st.plotly_chart(fig1, use_container_width=True)

col4, col5, col6 = st.columns([2, 2, 0.2])

#col4.text(" ")
col4.markdown('<a id="today"></a>', unsafe_allow_html=True)
col4.image(dci_finals, caption='DCI World Championship Finals Predictions')
col4.text(" ")
col4.text(" ")
col4.text(" ")
col4.text(" ")
col4.text(" ")
col4.text(" ")
col4.text(" ")
col4.text(" ")
col4.text(" ")


col4.markdown('<a id="max_rank"></a>', unsafe_allow_html=True)
col4.markdown("## Rank by Maximum Score To Date")
col4.image(max_rank_image, caption='Drum Corps Rank by Max Score to Date')

col4.markdown('<a id="finals"></a>', unsafe_allow_html=True)
col4.markdown('## Finals Predictions')
col4.image(finals_pred_image, caption='2022 Finals Predictions, Indianpolis, IN')

col4.markdown('<a id="pastpredictions"></a>', unsafe_allow_html=True)
col4.markdown('## Past Predictions')

col4.image(dci_semis, caption='DCI Semifinals Predictions')
col4.image(dci_prelims, caption='DCI Prelims Predictions')
col4.image(dci_austin, caption='DCI Austin Predictions')
col4.image(dci_denton, caption='DCI Denton Predictions')
col4.image(central_indiana_image, caption='2022 DCI Central Indiana Predictions, Muncie, IN')
col4.image(tour_premiere_image, caption='2022 DCI Tour Premiere Predictions, Detroit, MI')
col4.image(western_corps_connection_image, caption='2022 Western Corps Connections Predictions, San Bernardino, CA')
col4.image(drum_corps_at_the_rose_bowl_image, caption='2022 Drum Corps at the Rose Bowl Predictions, Pasadena, CA')
col4.image(corps_at_the_crest_image, caption='2022 Corps at the Crest Predictions, Vista, CA')