import streamlit as st

import pandas as pd
import plotly.express as px

dci_colors = pd.read_csv('pages/drum_corps_colors.csv')
color_discrete_map = dict(dci_colors.values)

st.set_page_config(page_title="Historical Scores", layout="wide")

score_df1 = pd.read_csv('pages/2013-to-2019-World-Class-DCI-scores.csv')
score_df2 = pd.read_csv('pages/2022-World-Class-DCI-scores.csv')
score_df3 = pd.read_csv('pages/2023-World-Class-DCI-scores.csv')
score_df = pd.concat([score_df1, score_df2, score_df3])
score_df['Date'] = pd.to_datetime(score_df.Date)
score_df['Year'] = score_df.Date.dt.year
score_df = score_df.sort_values(by=['Corps', 'Year']).reset_index(drop=True)
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
    annotation_xtext = 0.85
    annotation_ytext = -0.10
else:
    filtered_df = score_df[(score_df.Corps == corp) & (score_df.Date.dt.year == year)].reset_index(drop=True)
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
    title=f'{corp} Scores for {year}',
    font=dict(
        size=20
    )
).add_annotation(dict(font=dict(size=15),
                      x=annotation_xtext,
                      y=annotation_ytext,
                      showarrow=False,
                      text="Data: https://dci.org<br>Graphic:@Danger009Mouse",
                      textangle=0,
                      xanchor='left',
                      xref="paper",
                      yref="paper")
                 )

st.plotly_chart(fig2, use_container_width=True)
