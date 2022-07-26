import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pergunta_1
import pergunta_2
# import plotly.express as px

selection = st.sidebar.radio(" ", ["Inicio", "Pergunta 1", "Pergunta 2", "Pergunta 3"])



def inicio():
    st.title('Ánalise de dados do dataset "Heart_disease" para a cadeira PI3')

    dataframe = pd.read_csv('../heart_2020_cleaned.csv')

    chart_data = pd.DataFrame(list(zip(dataframe['BMI'].tolist(),dataframe['PhysicalHealth'].tolist(),dataframe['MentalHealth'].tolist())),
    columns = ['Body Mass Index (BMI)','PhysicalHealth','MentalHealth'])
    st.dataframe(dataframe.head())
    range_chart = st.slider('Quantidade de dados no gráfico', 0, 300, 30)
    st.area_chart(chart_data.head(range_chart))
    st.write('O objetivo deste trabalho será analisar e expôr aqui informações necessárias para a construção do artigo.')



if selection == "Pergunta 1":
    pergunta_1.pergunta1()
elif selection == "Inicio":
    inicio()
elif selection == "Pergunta 2":
    pergunta_2.pergunta_2()