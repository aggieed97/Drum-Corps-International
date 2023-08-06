import streamlit as st

import pandas as pd
import plotly.express as px

dci_colors = pd.read_csv('pages/drum_corps_colors.csv')
color_discrete_map = dict(dci_colors.values)

st.set_page_config(page_title="Caption Analysis", layout="wide")

df = pd.read_csv('pages/2023-DCI-Caption-Score-Recaps.csv')
larger_df = pd.read_csv('pages/2023-DCI-Caption-Score-Recaps-Large.csv')

df['date'] = pd.to_datetime(df.date)
larger_df['date'] = pd.to_datetime(larger_df.date)

cols = df.iloc[:, 12:].columns
larger_cols = larger_df.iloc[:, 12:].columns

df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
larger_df[larger_cols] = larger_df[larger_cols].apply(pd.to_numeric, errors='coerce')

corps = list(df.drum_corps.unique())
corps.sort()
#corps.insert(0, "All")

captions_list = ['General Effect Total', 'Visual Proficiency', 'Visual Analysis', 'Visual Color Guard',
                 'Visual Total', 'Music Brass', 'Music Analysis', 'Music Percussion', 'Music Total', 'Total']


def ge_scores_by_drum_corps(corp):
    larger_ge_df = larger_df[larger_df.drum_corps.isin(corp)].reset_index(drop=True)
    larger_ge_df = larger_ge_df[['date', 'location', 'drum_corps', 'general_effect1_judge', 'general_effect2_judge',
                                 'general_effect_total_score']]

    ge_df = df[df.drum_corps.isin(corp)].reset_index(drop=True)
    ge_df = ge_df[
        ['date', 'location', 'drum_corps', 'general_effect1_judge', 'general_effect2_judge',
         'general_effect_total_score']]

    final_df = pd.concat([ge_df, larger_ge_df]).sort_values(by='date')
    final_df = pd.concat([ge_df, larger_ge_df]).sort_values(by=['drum_corps', 'date'])
    final_df = final_df[(final_df != 0).all(1)].reset_index(drop=True)

    return final_df
    #return ge_df

def music_scores_by_drum_corps(corp='Blue Devils'):
    music_cols = ['date', 'location', 'drum_corps', 'music_brass_judge', 'music_analysis_judge',
                  'music_percussion_judge', 'music_brass_score', 'music_analysis_score', 'music_percussion_score',
                  'music_total_score']

    larger_music_df = larger_df[larger_df.drum_corps.isin(corp)].reset_index(drop=True)

    if larger_music_df['music_analysis2_score'][0] == 0:
        larger_music_df['music_analysis_score'] = (larger_music_df['music_analysis1_score'] + larger_music_df[
            'music_analysis2_score']) / 2
    else:
        larger_music_df['music_analysis_score'] = larger_music_df['music_analysis1_score']

    larger_music_df = larger_music_df[music_cols]

    music_df = df[df.drum_corps.isin(corp)].reset_index(drop=True)
    music_df = music_df[music_cols]

    final_df = pd.concat([music_df, larger_music_df]).sort_values(by=['drum_corps', 'date'])
    final_df = final_df[(final_df != 0).all(1)].reset_index(drop=True)

    return final_df
    #return music_df


def visual_scores_by_drum_corps(corp='Blue Devils'):
    visual_cols = ['date', 'location', 'drum_corps', 'visual_proficiency_judge', 'visual_analysis_judge',
                   'visual_color_guard_judge', 'visual_proficiency_score', 'visual_analysis_score',
                   'visual_color_guard_score', 'visual_total_score']

    visual_df = df[df.drum_corps.isin(corp)].reset_index(drop=True)

    visual_df = visual_df[visual_cols]

    larger_visual_df = larger_df[larger_df.drum_corps.isin(corp)].reset_index(drop=True)
    larger_visual_df = larger_visual_df[visual_cols]

    final_df = pd.concat([visual_df, larger_visual_df]).sort_values(by=['drum_corps', 'date'])
    final_df = final_df[(final_df != 0).all(1)].reset_index(drop=True)

    return final_df
    #return visual_df

def total_scores_by_drum_corps(corp):
    larger_ge_df = larger_df[larger_df.drum_corps.isin(corp)].reset_index(drop=True)

    larger_ge_df = larger_ge_df[['date', 'location', 'drum_corps', 'total_score']]

    ge_df = df[df.drum_corps.isin(corp)].reset_index(drop=True)
    ge_df = ge_df[['date', 'location', 'drum_corps', 'total_score']]

    final_df = pd.concat([ge_df, larger_ge_df]).sort_values(by=['drum_corps', 'date'])
    final_df = final_df[(final_df != 0).all(1)].reset_index(drop=True)

    return final_df
    #return ge_df

def get_line_chart(caption_picked):
    fig2 = px.line(
        data_frame=filtered_df,
        x='date',
        y=caption_picked,
        color='drum_corps',
        color_discrete_map=color_discrete_map,
        markers=True,
        hover_name='location',
        template='seaborn',
        labels={
            'drum_corps': 'Drum Corps',
            'date': 'Date'
        }
    ).update_layout(
        autosize=False,
        width=500,
        height=500,
        title=f'{caption} Scores for 2023',
        xaxis_title='Date',
        yaxis_title=f'{caption} Score',
        font=dict(
            size=20
        )
    ).add_annotation(dict(font=dict(size=15),
                          x=0.85,
                          y=-0.25,
                          showarrow=False,
                          text="Data: https://dci.org<br>Graphic: @Danger009Mouse",
                          textangle=0,
                          xanchor='left',
                          xref="paper",
                          yref="paper")
    )

    for i, d in enumerate(fig2.data):
        fig2.add_scatter(x=[d.x[-1]], y=[d.y[-1]],
                        mode='markers+text',
                        text=d.y[-1],
                        textfont=dict(color=d.line.color, size=10),
                        textposition='middle right',
                        marker=dict(color=d.line.color, size=10),
                        legendgroup=d.name,
                        showlegend=False)
    return fig2

col1, col2 = st.columns(2)

with col1:
    #corp = st.selectbox('Choose a Drum Corps:', corps)
    corp = st.multiselect('Choose your favorite Drum Corps:', corps)
with col2:
    caption = st.selectbox('Choose a Caption:', captions_list)

if caption == 'General Effect Total':
    filtered_df = ge_scores_by_drum_corps(corp=corp)
    filtered_df['date']=filtered_df['date'].astype(str)

    fig2 = get_line_chart(caption_picked='general_effect_total_score')
    st.plotly_chart(fig2, use_container_width=True)
    st.table(filtered_df)

elif 'Visual' in caption:
    filtered_df = visual_scores_by_drum_corps(corp=corp)
    filtered_df['date'] = filtered_df['date'].astype(str)

    if caption == 'Visual Proficiency':
        y = 'visual_proficiency_score'
    elif caption == 'Visual Analysis':
        y = 'visual_analysis_score'
    elif caption == 'Visual Color Guard':
        y = 'visual_color_guard_score'
    else:
        y = 'visual_total_score'

    fig2 = get_line_chart(caption_picked=y)

    st.plotly_chart(fig2, use_container_width=True)
    st.table(filtered_df)

elif 'Music' in caption:
    filtered_df = music_scores_by_drum_corps(corp=corp)
    filtered_df['date'] = filtered_df['date'].astype(str)

    if caption == 'Music Brass':
        y = 'music_brass_score'
    elif caption == 'Music Analysis':
        y = 'music_analysis_score'
    elif caption == 'Music Percussion':
        y = 'music_percussion_score'
    else:
        y = 'music_total_score'

    fig2 = get_line_chart(caption_picked=y)


    st.plotly_chart(fig2, use_container_width=True)
    st.table(filtered_df)

elif caption == 'Total':
    filtered_df = total_scores_by_drum_corps(corp=corp)
    filtered_df['date']=filtered_df['date'].astype(str)

    fig2 = get_line_chart(caption_picked='total_score')
    st.plotly_chart(fig2, use_container_width=True)
    st.table(filtered_df)

