import streamlit as st
import pandas as pd
import numpy as np

# App Name
st.title('Uber pickups in NYC')

# Fetch some data
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
DATA_FILE = 'uber-raw-data-sep14.csv'

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_FILE, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    
    return data

# Effortless caching
data = load_data(10000)


# Inspect data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# Draw a histogram
st.header("Number of pickups by hour")
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)


## Plot data on a map
hour_to_filter = st.slider('Hour', 0, 23, 17) 
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)