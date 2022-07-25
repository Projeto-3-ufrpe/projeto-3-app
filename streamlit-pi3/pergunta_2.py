import streamlit as st
from dataframe import Dados

def pergunta_2():
    st.title('Doenças provindas de outros órgãos do corpo, podem ser um indicativo de doenças cardíacas ?')
    df = Dados.dataframe
    #colunas para analisar, Diabetic, Asthma, SkinCancer, HeartDisease, 