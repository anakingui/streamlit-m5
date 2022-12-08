import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
titanic_link = 'titanic.csv'
titanic_data = pd.read_csv(titanic_link)
st.header('Dataset Overview')
st.dataframe(titanic_data)
fig, ax=plt.subplots()
ax.hist(titanic_data.Fare)
st.header('Histograma del Titanic')
st.pyplot(fig)
st.markdown('___')
fig2, ax2 =plt.subplots()
y_pos = titanic_data['Pclass']
x_pos = titanic_data['Fare']
ax2.barh(y_pos, x_pos)
ax2.set_ylabel('Pclass')
ax2.set_xlabel('Fare')
ax2.set_title('¿Cuánto pagaron las clases del Titanic?')
st.header('Gráfica de barras del Titanic')
st.pyplot(fig2)
st.markdown('____')
fig3, ax3 = plt.subplots()
ax3.scatter(titanic_data.Age, titanic_data.Fare)
ax3.set_xlabel('Edad')
ax3.set_ylabel('Tarifa')
st.header('Gráfica de dispersión del Titanic')
st.pyplot(fig3)