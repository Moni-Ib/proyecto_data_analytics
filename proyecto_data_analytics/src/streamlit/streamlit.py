import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title('Proyecto Programación')
st.markdown('Mónica Ibarra Herrera')

st.header("Data set")
df = pd.read_csv("C:/Users/cesar/apps/proyecto_data_analytics/proyecto_data_analytics/src/streamlit/df_corregido.csv") 
df.columns=["year","country","city","stage","home_team","away_team","home_score","away_score","outcome","winning_team","losing_team","date", "month", "dayofweek"] 
st.dataframe(df)
print('\n')

st.header("Partidos de México")
df = pd.read_csv("C:/Users/cesar/apps/proyecto_data_analytics/proyecto_data_analytics/src/streamlit/partidos_mex.csv") 
df.columns=["year","country","city","stage","home_team","away_team","home_score","away_score","outcome","winning_team","losing_team","date", "month", "dayofweek"] 
st.dataframe(df)
print('\n')



