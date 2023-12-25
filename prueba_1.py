

import streamlit as st
import pandas as pd

st.set_page_config(page_title="prueba_1")

dataset = st.container()
dim = st.container()

with dataset:
    data = pd.read_csv('/Users/javi/Documents/APP/prueba_1/data/customers.csv',delimiter=",", decimal=".")
    st.write(data.head(20))     

with dim:
    st.markdown('#### Dimensión de la información')
    code = '''data.shape'''
    st.code(code, language='python')
    st.write(data.shape)
