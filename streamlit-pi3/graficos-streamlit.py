from ast import With
from tkinter import W
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pergunta_1
import pergunta_2


opcoes = ["Inicio", "🧑 Caracteristicas imutaveis", "🧠 Deonças vindas de outros orgãos ", "⛹️ Hábitos"]
with st.sidebar:
    
    st.markdown('# 🆙GRUPO UPSCALE ')
    st.markdown('## MENU PRINCIPAL 👈')
    selection = st.radio("", opcoes)
# selection = st.sidebar



def inicio():
    st.markdown('# 🆙GRUPO UPSCALE')
    st.title('Ánalise de dados para a cadeira PI3')
    st.markdown('### A ánalise dos dados do conjunto de dados HEART_DISEASE tem como o objetivo fazer o uso de um olhar critico e questionador sobre os dados encontrados para que através desta analise seja possivel responder as perguntas deste trabalho e chegar a uma conclusão satisfatoria.')
    st.markdown('### As perguntas são 3: ')
    st.markdown('- É correto afirmar que características imutáveis dos indivíduos podem indicar que eles possuem ou podem vir a possuir doenças cardíacas? E existe algum fator que acompanhe essas características com frequência?')
    st.markdown('- Doenças provindas de outros órgãos do corpo, podem ser um indicativo de doenças cardíacas ?')
    st.markdown('- É possível prever que um indivíduo tem um grande potencial de ter uma doença cardíaca a partir dos seus hábitos?')

    dataframe = pd.read_csv('../heart_2020_cleaned.csv')

    chart_data = pd.DataFrame(list(zip(dataframe['BMI'].tolist(),dataframe['PhysicalHealth'].tolist(),dataframe['MentalHealth'].tolist())),
    columns = ['Body Mass Index (BMI)','PhysicalHealth','MentalHealth'])
    st.dataframe(dataframe.head())
    range_chart = st.slider('Quantidade de dados no gráfico', 0, 300, 30)
    st.area_chart(chart_data.head(range_chart))
    st.write('O objetivo deste trabalho será analisar e expôr aqui informações necessárias para a construção do artigo.')



if selection == "Caracteristicas imutaveis":
    pergunta_1.pergunta1()
elif selection == "Inicio":
    inicio()
elif selection == "Deonças vindas de outros orgãos":
    pergunta_2.pergunta_2()