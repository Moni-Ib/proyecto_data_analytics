import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


st.title("Análisis Titanic")
st.markdown("*Mónica Ibarra Herrera*")
st.image('mundial-foto,jpg')
st.header("Data Set")

df = pd.read_csv("wcmatches.csv") 
st.dataframe(df)
print('\n')

st.header("Histograma sobrevivientes")
survived_agrupado = df.groupby("survived")
fig, ax = plt.subplots(figsize=(6,4))
for i, survived_agrupado in survived_agrupado:
    ax.hist(survived_agrupado["survived"], alpha = 0.5, bins=2, label=str(i))
ax.set_title('Sobrevivientes', fontname= 'Times New Roman', fontsize= 15)
ax.set_xlabel('0 No sobrevivieron, 1 Sobrevivieron', fontname= 'Times New Roman', fontsize=12)
ax.legend()
st.pyplot(fig)
st.markdown("*Hallazgo del histograma*")
st.markdown("Como podemos ver la mayoría de los pasajeros no sobrevivió, más de 500 murieron.")