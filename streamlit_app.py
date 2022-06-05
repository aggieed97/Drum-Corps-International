import streamlit as st

import pandas as pd
import plotly.express as px

champions = pd.read_csv('DCI-World-Champions-1972-2019.csv')
champions = champions.rename(columns={'Champion & Repertoire': 'Drum Corps'})

dci_colors = pd.read_csv('drum_corps_colors.csv')
color_discrete_map = dict(dci_colors.values)

st.set_page_config(page_title="DCI App", layout="wide")

colT1, colT2 = st.columns([1, 2])
with colT2:
    st.title("Drum Corps International")

score_df = pd.read_csv('2013-to-2019-World-Class-DCI-scores.csv')
score_df['Date'] = pd.to_datetime(score_df.Date)
score_df['Year'] = score_df.Date.dt.year
score_df = score_df.sort_values(by=['Corps', 'Year']).reset_index(drop =True)
corps = list(score_df.Corps.unique())
corps.insert(0, "All")
years = list(score_df.Year.unique())

st.title('World Class Drum Corps Scores by Year')

col1, col2 = st.columns(2)

with col1:
    corp = st.selectbox('Choose a Drum Corps:', corps)
with col2:
    year = st.selectbox('Choose a Year:', years)

if corp == 'All':
    filtered_df = score_df[score_df.Date.dt.year == year].reset_index(drop=True)
    height = 900
else:
    filtered_df = score_df[(score_df.Corps == corp) & (score_df.Date.dt.year == year)].reset_index(drop=True)
    height = 500

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
    title=f'{corp} Scores for {year}',
    font=dict(
        size=20
            )
).add_annotation(dict(font=dict(color='white', size=15),
                                 x=0.85,
                                 y=-0.13,
                                 showarrow=False,
                                 text="Data: https://dci.org<br>Graphic:@Danger009Mouse",
                                 textangle=0,
                                 xanchor='left',
                                 xref="paper",
                                 yref="paper")
                )

st.plotly_chart(fig2, use_container_width=True)

st.title('World Class Drum Corps Champions by Year')
st.dataframe(champions)

st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")

fig1 = px.histogram(
    data_frame=champions,
    y='Drum Corps',
    color='Drum Corps',
    color_discrete_map=color_discrete_map,
).update_layout(
    title={
        'text': 'Drum Corps International <br>World Class Championship Titles 1972-2019*',
        'y': 0.97,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title='Championship Title Count',
    yaxis_title='Drum Corps',
    font=dict(
        size=18,
    ),
    width=500,
    height=1000,
    showlegend=False,
    margin=dict(
        l=25,
        r=25,
        b=100,
        t=100,
        pad=4
    )
).update_yaxes(
    categoryorder="total ascending"
).update_traces(hovertemplate='<i>Championships</i>: ' + '%{x}' + '<extra></extra>',
                selector=dict(type="histogram")
                ).add_annotation(dict(font=dict(color='white', size=15),
                                      x=0,
                                      y=-0.12,
                                      showarrow=False,
                                      text="* Including Ties in 1996, 1999, & 2000",
                                      textangle=0,
                                      xanchor='left',
                                      xref="paper",
                                      yref="paper")
                                 ).add_annotation(dict(font=dict(color='white', size=15),
                                                       x=0.6,
                                                       y=-0.13,
                                                       showarrow=False,
                                                       text="Data: https://en.wikipedia.org/wiki/Drum_Corps_International_World_Class_Champions<br>Graphic:@Danger009Mouse",
                                                       textangle=0,
                                                       xanchor='left',
                                                       xref="paper",
                                                       yref="paper")
                                                  )

st.plotly_chart(fig1, use_container_width=True)
