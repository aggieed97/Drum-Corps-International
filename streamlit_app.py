import streamlit as st

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

import pandas as pd
import plotly.express as px

import warnings
warnings.filterwarnings("ignore")

url = 'https://en.wikipedia.org/wiki/Drum_Corps_International_World_Class_Champions'

uClient = uReq(url) # opening up connection, grabbing the page
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

table = page_soup.find_all("table")
champions = pd.read_html(str(table), header = 0)[0]

#https://stackoverflow.com/questions/42205616/using-str-split-for-pandas-dataframe-values-based-on-parentheses-location
champions['Champion & Repertoire'] = champions['Champion & Repertoire'].str.split("\s+\(").str[0]

champions['Champion & Repertoire'] = champions['Champion & Repertoire'].replace('The Cadets of Bergen County', 'The Cadets')
champions['Champion & Repertoire'] = champions['Champion & Repertoire'].replace('Garfield Cadets', 'The Cadets')

champions = champions[2:].copy().reset_index(drop = True)

ties = [pd.Series([2000, '12 August', 'The Cavaliers', 97.650, 'College Park, Maryland', 'Byrd Stadium'],
                  index=champions.columns ),
                pd.Series([1999, '14 August', 'Santa Clara Vanguard', 98.400, 'Madison, Wisconsin', 'Camp Randall Stadium'],
                          index=champions.columns ),
                pd.Series([1996, '17 August', 'Phantom Regiment', 97.400, 'Orlando, Florida', 'Citrus Bowl'],
                          index=champions.columns ),
       ]

champions = champions.append(ties, ignore_index=True)

champions = champions.rename(columns = {'Champion & Repertoire':'Drum Corps'})

dci_colors = pd.read_csv('drum_corps_colors.csv')
color_discrete_map = dict(dci_colors.values)

st.set_page_config(page_title="DCI App", layout="wide")

colT1,colT2 = st.columns([1,8])
with colT2:
    st.title("Drum Corps International")

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
    color_discrete_map=color_discrete_map
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
        size = 18,
        color='white'
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
).update_traces(hovertemplate ='<i>Championships</i>: ' + '%{x}' + '<extra></extra>',
                  selector=dict(type="histogram")
).add_annotation(dict(font=dict(color='white',size=15),
                                        x=0,
                                        y=-0.12,
                                        showarrow=False,
                                        text="* Including Ties in 1996, 1999, & 2000",
                                        textangle=0,
                                        xanchor='left',
                                        xref="paper",
                                        yref="paper")
).add_annotation(dict(font=dict(color='white',size=15),
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