

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title="ALAUNA")

header = st.container()
traduccion = st.container()
presenta = st.container()
dataset = st.container()
info = st.container()
dim = st.container()
info_cuali = st.container()
pie_1 = st.container()
pregunta_1 = st.container()
pie_2 = st.container()
cuali_por2 = st.container()
box = st.container()

with header:
    st.markdown('# Customers')
    st.markdown('Consumer behaviour is the study of how people buy, what they buy, when they buy and why they buy. **Philip Kotler**.')

with traduccion:
    traduce = st.checkbox('Traducir cita')
    if traduce:
        st.write('El comportamiento del consumidor es el estudio de cómo compran las personas, qué compran, cuándo compran y por qué compran. **Philip Kotler**.')

with presenta:
    st.markdown('#### Información')

with dataset:
    url = "https://raw.githubusercontent.com/usebien/prueba_3/main/customers.csv"
    data = pd.read_csv(url)
    st.write(data.head(20))        

with info:
    st.markdown('¿**Información** completa?')
    code = '''data.isna().sum()'''
    st.code(code, language='python')
    st.write(data.isna().sum())

with dim:
    st.markdown('#### Dimensión de la información')
    code = '''data.shape'''
    st.code(code, language='python')
    st.write(data.shape)


with info_cuali:
    st.markdown('#### Información cualitativa')
    st.markdown('Solo una variable cualitativa:')
    st.markdown('Observando los porcentajes por modadlidades, ¿se trata de una muestreo aleatoria?')

with pie_1:
    fig = px.pie(data.groupby(['Gender'])['Gender'].count().reset_index(name='count'), values='count', names='Gender', title='Gender')
    st.plotly_chart(fig.update_traces(textposition='inside', textfont_size=24), theme="streamlit")

with pregunta_1:
    pregunta = st.checkbox('Toca para desplegar una **pregunta** sobre el diagrama de sectores.')
    if pregunta:
        st.write('Observando los porcentajes de las modalidades obtenidos, ¿se tratará de una muestra aleatoria o no aleatoria?. ¿Podríamos considerar un muetreo aleatorio simple, o un muestreo estratificado o bien por cuotas')

with pie_2:
    fig = px.pie(data.groupby(['Profession'])['Profession'].count().reset_index(name='count'), values='count', names='Profession', title='Profession')
    st.plotly_chart(fig.update_traces(textposition='inside', textfont_size=24), theme="streamlit")

with cuali_por2:
    fig = px.histogram(data, x="Gender", y="Annual Income ($)",
             color='Profession', barmode='group',
             height=400)
    st.plotly_chart(fig.update_traces(textposition='inside', textfont_size=20), theme="streamlit")

with box:
    st.markdown('#### lo que sigue')
    fig = px.box(data, y ='Gender',  x = 'Annual Income ($)', color= 'Gender', orientation='h')
    st.plotly_chart(fig, theme="streamlit")

with box:
    st.markdown('#### lo que sigue, macaya')
    fig = px.box(data, y ='Annual Income ($)',  x = 'Profession', color= 'Profession')
    st.plotly_chart(fig, theme="streamlit")

