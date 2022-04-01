import streamlit as st
import pandas as ps 

df = pd.read_csv("https://raw.githubusercontent.com/a349288/mapa/main/data.csv")
st.write(df)
st.map(df)
