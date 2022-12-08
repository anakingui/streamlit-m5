import pandas as pd
import streamlit as st

#def load_data(nrows):
 #   data = pd.read_csv(DATA_URL, 
 #   nrows=nrows)
 #   return data
walmart_data = 'walmart.csv'
walmart = pd.read_csv(walmart_data)

st.title('Datos de Walmart' )
st.header("Datos de tiendas walmart")
st.write("""Predicción de ventas de productos de linea
               blanca en el noroeste de los Estados Unidos""")
st.dataframe(walmart)
sidebar = st.sidebar

# Titulo de la barra lateral
sidebar.title("Esta es la barra lateral")
selected_class = sidebar.radio('Ship Mode',walmart['Ship Mode'].unique())
sidebar.write('Ship Mode:', selected_class)
category = sidebar.selectbox('Category',walmart['Category'].unique())
sidebar.write(f'Selected Category:{category!r}')
optionals = sidebar.expander('Discount', True)
select=optionals.slider(
     'Select the discount', min_value= float(walmart['Discount'].min()),
     max_value= float(walmart['Discount'].max())
     )
subset = walmart[(walmart['Discount']>= select)]
sidebar.write(f"{select}:{subset.shape[0]}")