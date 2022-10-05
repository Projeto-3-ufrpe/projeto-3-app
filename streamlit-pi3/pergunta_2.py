import streamlit as st
from dataframe import Dados
import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt

def pie_chart_com_doenca(coluna):#quantidade
    labels = f'Possui {coluna}', f'Não possui {coluna}'
    df_limitado = Dados.dataframe.query("HeartDisease == 1")
    df_com_doenca_coracao_e_outra_doenca = df_limitado.query(f"{coluna} == 1")
    porcentagem_possui_outra_doenca = len(df_com_doenca_coracao_e_outra_doenca.index) / len(df_limitado.index)
    sizes = [porcentagem_possui_outra_doenca, 1 - porcentagem_possui_outra_doenca]
    explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)

def pie_chart_sem_doenca(coluna): #quantidade
    labels = f'Possui {coluna}', f'Não possui {coluna}'
    df_limitado = Dados.dataframe.query("HeartDisease == 0")
    # st.dataframe(df_limitado)
    df_sem_doenca_coracao_e_com_outra_doenca = df_limitado.query(f"{coluna} == 1")
    porcentagem_possui_outra_doenca = len(df_sem_doenca_coracao_e_com_outra_doenca.index) / len(df_limitado.index)
    sizes = [porcentagem_possui_outra_doenca, 1 - porcentagem_possui_outra_doenca]
    explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)


def pergunta_2():
    st.title('Doenças provindas de outros órgãos do corpo, podem ser um indicativo de doenças cardíacas ?')
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Dados com indivíduos que têm ou já tiveram alguma doença no coração')
        # range_chart_com_doenca = st.slider('Quantidade de dados no gráfico de indivíduos com doença no coração', 0, len(Dados.df_somente_com_doencas_do_coracao.index), 27373)
        pie_chart_com_doenca('Diabetic')
        pie_chart_com_doenca('Asthma')
        pie_chart_com_doenca('SkinCancer')

    with col2:
        st.subheader('Dados com indivíduos que não possui nenhuma doença no coração')
        # range_chart_sem_doenca = st.slider('Quantidade de dados no gráfico de indivíduos sem doença no coração', 0, len(Dados.df_somente_sem_doencas_do_coracao.index), 27373)
        pie_chart_sem_doenca('Diabetic')
        pie_chart_sem_doenca('Asthma')
        pie_chart_sem_doenca('SkinCancer')
    st.subheader(f'''Analisando os gráficos com a mesma quantidade de indivíduos que já tiveram e que não tiveram doença cardíeca
    Podemos supor que há um leve indicativo de ter uma doença do coração já tendo uma das três doenças analisadas, com uma maior
    ênfase em Diabetes.''')
    st.subheader(f'''Abaixo está uma imagem de dados de um jovem saudável que não teve diabetes''')
    st.image('./assets/predicao-sem-diabetes.jpg')
    st.subheader(f'''E abaixo está a mesma predição, só mudando o diabetes para sim''')
    st.image('./assets/predicao-com-diabetes.jpg')
    st.subheader('''Note que aumentou em média 3 por cento por um jovem saudável''')
        



    #colunas para analisar, Diabetic, Asthma, SkinCancer, HeartDisease, 