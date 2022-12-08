import pandas as pd
import numpy as np
import streamlit as st

st.title('Análisis de Uber')
st.header('Nueva York')
st.write('''Estudio de viajes de Uber en la 
           ciudad de Nueva York''')
uber = ('uber-raw-data-sep14.csv')
Date='date/time'


@st.cache
def load_data(nrows):
    uber_data = pd.read_csv(uber, nrows=nrows)
    # es necesario porque todos los datos se requieren en
    # minusculas en st.map
    lowercase = lambda x : str(x).lower() 
    uber_data.rename(lowercase,axis='columns', inplace=True)
    uber_data[Date]=pd.to_datetime(uber_data[Date])
    return uber_data

data_load_state = st.text('Loading data...')
uber_data = load_data(1000)
data_load_state.text("Done! using st.cache")

hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = uber_data[uber_data[Date].dt.hour == hour_to_filter]
st.subheader('Mapa de recogidas a %s:00' % hour_to_filter)
st.map(filtered_data)

#hour_travel=optionals.slider(
#      'Hour', min_value= float(hour.min()),
  #    max_value= float(walmart['Discount'].max())
   #   )
# subset = walmart[(walmart['Discount']>= select)]
# sidebar.write(f"{select}:{subset.shape[0]}")