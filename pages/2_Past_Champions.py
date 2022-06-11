import streamlit as st
from st_aggrid import AgGrid

import pandas as pd
import plotly.express as px

champions = pd.read_csv('pages/DCI-World-Champions-1972-2019.csv')
champions = champions.rename(columns={'Champion & Repertoire': 'Drum Corps'})

dci_colors = pd.read_csv('pages/drum_corps_colors.csv')
color_discrete_map = dict(dci_colors.values)

st.set_page_config(page_title="DCI Past Champions", layout="wide")

st.title('World Class Drum Corps Champions by Year')

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
                                                       x=0.5,
                                                       y=-0.13,
                                                       showarrow=False,
                                                       text="Data: https://en.wikipedia.org/wiki/Drum_Corps_International_World_Class_Champions<br>Graphic:@Danger009Mouse",
                                                       textangle=0,
                                                       xanchor='left',
                                                       xref="paper",
                                                       yref="paper")
                                                  )

st.plotly_chart(fig1, use_container_width=True)
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")
AgGrid(champions)
