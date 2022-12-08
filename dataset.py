import pandas as pd
import streamlit as st

def load_data(nrows):
    data = pd.read_csv(DATA_URL, 
    nrows=nrows)
    return data


names_link = 'dataset.csv'
names_data = pd.read_csv(names_link)

st.title('streamlit con pandas' )
st.dataframe(names_data)