import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

st.title('Proyecto Programación')
st.markdown('Mónica Ibarra Herrera')

st.header("Data set")
df = pd.read_csv("C:/Users/cesar/apps/proyecto_data_analytics/proyecto_data_analytics/src/streamlit/df_corregido.csv") 
df.columns=["year","country","city","stage","home_team","away_team","home_score","away_score","outcome","winning_team","losing_team","date", "month", "dayofweek"] 
st.dataframe(df)
print('\n')

st.header("Partidos de México")
df_mexico = pd.read_csv("C:/Users/cesar/apps/proyecto_data_analytics/proyecto_data_analytics/src/streamlit/partidos_mex.csv") 
df_mexico.columns=["year","country","city","stage","home_team","away_team","home_score","away_score","outcome","winning_team","losing_team","date", "month", "dayofweek"] 
st.dataframe(df_mexico)
print('\n')

#Visualizaciones países
st.header("Mundiales ganados por países")
finales= df[df['stage']=='Final']
ganadores_finales = finales['winning_team'].value_counts()
ganadores_finales
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=ganadores_finales.index, y=ganadores_finales.values, palette="viridis", ax=ax)
plt.title('Mundiales ganados por países')
plt.xlabel('Países')
plt.ylabel('# de Mundiales')
plt.xticks(rotation=45)
st.pyplot(fig)
st.markdown("**Brasil es el país que ha ganado más mundiales, superando a los demás países con 5 victorias en total**")

#Visualizaciones México

st.header("Visualizaciones de México")
goles = df_mexico.groupby('year')[['home_score', 'away_score']].sum().sum(axis=1)
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=goles.index, y=goles.values, palette="viridis", ax=ax)
plt.title('Goles de México en los mundiales')
plt.xlabel('Año')
plt.ylabel('# de Goles')
plt.xticks(rotation=45)
st.pyplot(fig)

mexico_goals_home = df[df['home_team'] == 'Mexico']['home_score']
mexico_goals_away = df[df['away_team'] == 'Mexico']['away_score']
total_goles_mex = mexico_goals_home.sum() + mexico_goals_away.sum()
promedio_goles_mexico = total_goles_mex / len(df_mexico)

st.markdown("Promedio de goles metidos por México: {:.2f}".format(promedio_goles_mexico))

st.subheader('**Goles de México como local**')
fig, ax = plt.subplots(figsize=(8, 6))
ax.boxplot(mexico_goals_home)
ax.set_title('Goles de México como Local')
ax.set_ylabel('Goles')
st.pyplot(fig)
st.markdown('**México metió 4 goles cuando jugó contra el Salvador. El Salvador no ha ganado ningún partido**')
st.markdown('**México metió 3 goles cuando jugó contra Iran. Iran ha ganado sólo 2 partidos en los 21 mundiales**')

st.subheader('**Goles de México como visitante**')
fig, ax = plt.subplots(figsize=(8, 6))
ax.boxplot(mexico_goals_away)
ax.set_title('Goles de México como visitante')
ax.set_ylabel('Goles')
st.pyplot(fig)

st.subheader('México en las etapas de los mundiales')
participacion = df_mexico['stage'].value_counts()
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=participacion.index, y=participacion.values, palette="viridis", ax=ax)
ax.set_title('Frecuencia de Participación de México en Diferentes Etapas del Torneo')
ax.set_xlabel('Etapa del Torneo')
ax.set_ylabel('Partidos')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)
st.markdown('**México ha llegado hasta cuartos de final 2 veces**')

st.subheader('Cuartos de final México')
partidos_mexico_cuartos = df[(df['stage']=='Quarterfinals') & ((df['home_team'] == 'Mexico') | (df['away_team']=='Mexico'))]
st.dataframe(partidos_mexico_cuartos)
st.markdown('**Los 2 cuartos de finales, han sido en México**')