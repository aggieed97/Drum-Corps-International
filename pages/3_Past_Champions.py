import streamlit as st

import pandas as pd
import numpy as np
import plotly.express as px

champions = pd.read_csv('pages/DCI-World-Champions-1972-2019.csv')
champions = champions.rename(columns={'Champion & Repertoire': 'Drum Corps'})
champions = champions.sort_values(by='Year')
champions.index = np.arange(1, len(champions) + 1)

dci_colors = pd.read_csv('pages/drum_corps_colors.csv')
color_discrete_map = dict(dci_colors.values)

st.set_page_config(page_title="DCI Past Champions", layout="wide")

st.title('World Class Drum Corps Championship History')

fig1 = px.histogram(
    data_frame=champions,
    y='Drum Corps',
    color='Drum Corps',
    color_discrete_map=color_discrete_map,
).update_layout(
    title={
        'text': 'Drum Corps International <br>World Class Championship Titles 1972-2022*',
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
st.title('World Class Champions by Year')
caption_text = 'Including Ties in 1996, 1999, & 2000'

def highlight_cols(s, coldict):
    return ['background-color: {}'.format(color_discrete_map[v]) if v else '' for v in
            champions['Drum Corps'].isin(color_discrete_map.keys()) * champions['Drum Corps'].values]

champion_df = champions.style.set_caption(caption_text).hide_index() \
    .apply(highlight_cols, coldict=color_discrete_map) \
    .format({'Score':'{:.5}'}) \
    .set_table_styles([dict(selector='th', props=[('text-align', 'center')])]) \
    .set_table_styles([{'selector': 'th.col_heading', 'props': 'text-align: center;'}], overwrite = False)

#st.write(champion_df.to_html(index=False), unsafe_allow_html=True)
st.write(champion_df.to_html(), unsafe_allow_html=True)