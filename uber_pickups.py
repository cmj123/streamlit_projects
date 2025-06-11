import streamlit as st
import pandas as pd
import numpy as np

# App Name
st.title('Uber pickups in NYC')

# Fetch some data
DATA_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
DATA_FILE = 'uber-raw-data-sep14.csv'

def load_data(nrows):
    data = pd.read_csv(DATA_FILE, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATA_COLUMN] = pd.to_datetime(data[DATA_COLUMN])
    return data

data_load_state = st.text('Loading data... ')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")
data