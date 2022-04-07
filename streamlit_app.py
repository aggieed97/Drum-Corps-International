import streamlit as st

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

st.set_page_config(page_title="DCI App", layout="wide")

colT1,colT2 = st.columns([1,8])
with colT2:
    st.title("Drum Corps International")

st.dataframe(champions)

fig, ax = plt.subplots(figsize=(15,10))
ax = sns.countplot(y="Champion & Repertoire",
                   data=champions,
                   order=champions['Champion & Repertoire'].value_counts().index)

ax.set_title('Drum Corps International \nWorld Class Championship Titles 1972-2019*')
ax.set_ylabel('Drum Corps')
ax.set_xlabel('Championship Title Count', loc='left')
ax.set_xticks(range(0, 21))

rects = ax.patches

# For each bar: Place a label
for rect in rects:
    # Get X and Y placement of label from rect.
    x_value = rect.get_width()
    y_value = rect.get_y() + rect.get_height() / 2

    # Number of points between bar and label. Change to your liking.
    space = 5
    # Vertical alignment for positive values
    ha = 'left'

    # If value of bar is negative: Place label left of bar
    if x_value < 0:
        # Invert space to place label to the left
        space *= -1
        # Horizontally align label at right
        ha = 'right'

    # Use X value as label and format number with one decimal place
    label = "{:.0f}".format(x_value)

    # Create annotation
    plt.annotate(
        label,  # Use `label` as label
        (x_value, y_value),  # Place label at end of the bar
        xytext=(space, 0),  # Horizontally shift label by `space`
        textcoords="offset points",  # Interpret `xytext` as offset in points
        va='center',  # Vertically center label
        ha=ha)  # Horizontally align label differently for
    # positive and negative values.

plt.figtext(.48, .005,
            'Data: https://en.wikipedia.org/wiki/Drum_Corps_International_World_Class_Champions\nGraphic:@Danger009Mouse',
            fontsize=12)
plt.figtext(.08, .0003, '* Including Ties in 1996, 1999, & 2000', fontsize=12)

st.pyplot(fig = fig)