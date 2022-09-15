import streamlit as st
import dataframe 

def testeVoce():
    df = dataframe.balanceamentoDados()
    col1, col2, col3 = st.columns(3)
    with col1:
        grupos_raciais = df['Race'].unique().tolist()
        option_race = st.selectbox(
        'Selecione o grupo racial :',
        grupos_raciais)
        
    with col2:
        option_sex = st.radio("Selecione o sexo dos individuos", ["Female", "Male"])
    
    with col3:
        grupos_etarios = df['AgeCategory'].unique().tolist()
        option_age = st.selectbox(
        'Selecione a faixa etaria:',
        grupos_etarios)