import streamlit as st
from dataframe import Dados
import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt

def pie_chart_com_doenca(coluna,quantidade):
    labels = f'Possui {coluna}', f'Não possui {coluna}'
    df_limitado = Dados.df_somente_com_doencas_do_coracao.head(quantidade)
    df_com_doenca_coracao_e_outra_doenca = df_limitado.query(f"{coluna} == 'Yes'")
    porcentagem_possui_outra_doenca = len(df_com_doenca_coracao_e_outra_doenca.index) / len(df_limitado.index)
    sizes = [porcentagem_possui_outra_doenca, 1 - porcentagem_possui_outra_doenca]
    explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)

def pie_chart_sem_doenca(coluna,quantidade):
    labels = f'Possui {coluna}', f'Não possui {coluna}'
    df_limitado = Dados.df_somente_sem_doencas_do_coracao.head(quantidade)
    df_sem_doenca_coracao_e_com_outra_doenca = df_limitado.query(f"{coluna} == 'Yes'")
    porcentagem_possui_outra_doenca = len(df_sem_doenca_coracao_e_com_outra_doenca.index) / len(df_limitado.index)
    sizes = [porcentagem_possui_outra_doenca, 1 - porcentagem_possui_outra_doenca]
    explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)


def pergunta_2():
    st.title('Doenças provindas de outros órgãos do corpo, podem ser um indicativo de doenças cardíacas?')
    st.write('Primeiro vamos separar o Dataset em pessoas que tiveram doenças do coração e pessoas que não tiveram, e analisar as outras doenças desses dois grupos.')
    st.title('Com Doenças no coração, Quantidade: {}'.format(len(Dados.df_somente_com_doencas_do_coracao.index)))
    st.dataframe(Dados.df_somente_com_doencas_do_coracao)
    st.title('Sem Doenças no coração, Quantidade: {}'.format(len(Dados.df_somente_sem_doencas_do_coracao.index)))
    st.dataframe(Dados.df_somente_sem_doencas_do_coracao)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Dados com indivíduos que têm ou já tiveram alguma doença no coração')
        range_chart_com_doenca = st.slider('Quantidade de dados no gráfico de indivíduos com doença no coração', 0, len(Dados.df_somente_com_doencas_do_coracao.index), 27373)
        pie_chart_com_doenca('Diabetic',range_chart_com_doenca)
        pie_chart_com_doenca('Asthma',range_chart_com_doenca)
        pie_chart_com_doenca('SkinCancer',range_chart_com_doenca)

    with col2:
        st.subheader('Dados com indivíduos que não possui nenhuma doença no coração')
        range_chart_sem_doenca = st.slider('Quantidade de dados no gráfico de indivíduos sem doença no coração', 0, len(Dados.df_somente_sem_doencas_do_coracao.index), 27373)
        pie_chart_sem_doenca('Diabetic',range_chart_sem_doenca)
        pie_chart_sem_doenca('Asthma',range_chart_sem_doenca)
        pie_chart_sem_doenca('SkinCancer',range_chart_sem_doenca)

    st.markdown('### Considerando as 3 doenças presentes em nosso dataframe que originam de outros orgãos, iremos analisar a probabilidade de um individuo que possui cada uma delas e comparar com um que não possui.')
    st.dataframe(Dados.dataframe_sem_tratamento.iloc[-1:])
    linha_sem_tratamento = pd.DataFrame([[option_HeartDisease,option_bmi,option_smoking,option_AlcoholDrinking,option_stroke,option_PhysicalHealth,option_MentalHealth,option_DiffWalking,option_sex,option_age,option_race,option_Diabetic,option_PhysicalActivity,option_GenHealth,option_SleepTime,option_Asthma,option_KidneyDisease,option_SkinCancer]], columns=['HeartDisease','BMI','Smoking','AlcoholDrinking','Stroke','PhysicalHealth','MentalHealth','DiffWalking','Sex','AgeCategory','Race','Diabetic','PhysicalActivity','GenHealth','SleepTime','Asthma','KidneyDisease','SkinCancer'])
    dataframe_sem_tratamento_concatenado = dataframe.dataframe_nao_numerico.append(linha_sem_tratamento)
    linha_com_tratamento = dataframe.returnDataFrame(dataframe_sem_tratamento_concatenado)
        #criar metodo para treinar a regressao logisticar e usar o predict nessa linha_com_tratamento
    regressao_logistica = regressao_logistica_treinada()
    previsao = regressao_logistica.predict_proba(linha_com_tratamento.iloc[[-1]].drop('HeartDisease', axis=1))
    st.subheader(f'Voce tem {float(previsao[0][1]) * 100:.3f}% de chance de ter uma doenca cardieca segundo nosso algoritmo! :)')
    st.subheader(f'''Analisando os gráficos com a mesma quantidade de indivíduos que já tiveram e que não tiveram doença cardíeca
    Podemos supor que há um leve indicativo de ter uma doença do coração já tendo uma das três doenças analisadas, com uma maior
    ênfase em Diabetes, podemos ver que 10.4% dos indivíduos que não tiveram doenças do coração, tem diabetes,
    enquanto 32.7% das pessoas que tiveram doenças do coração também tiveram Diabetes, uma diferença de 22,3%, enquanto as outras 
    duas doenças tem uma porcentagem maior de em média 6,5% para pessoas que já tiveram doenças no coração comparado ao que não tiveram.''')
        



    #colunas para analisar, Diabetic, Asthma, SkinCancer, HeartDisease, 