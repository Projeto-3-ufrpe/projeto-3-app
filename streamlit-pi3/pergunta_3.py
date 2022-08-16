import streamlit as st
from dataframe import Dados
import pandas as pd
import plotly.express as px

def pergunta3():

    st.title("⛹️ Análise de Hábitos")
    st.write("***")

    st.markdown('### Pergunta 3: ')
    st.write("É possível prever que um indivíduo tem um grande potencial de ter uma doença cardíaca a partir dos seus hábitos ?")
    st.write("R: Analisar os dados referentes a qualidade de vida do indivíduo, como Consumo de álcool, tabagismo, tempo de sono, atividade Física e idade, e procurar padrões quantitativos que mais apresentam doenças cardíacas.")
    
    st.write("***")

    dataframe = pd.read_csv('../heart_2020_cleaned.csv')


    st.markdown('### Fumante ')
    #count_sexMale = int(dataframe[(dataframe["Smoking"] == "Yes") & (dataframe["Sex"] == "Male") & (dataframe["HeartDisease"] == "Yes")]["Smoking"].count())
    #count_sexFemale = int(dataframe[(dataframe["Smoking"] == "Yes") & (dataframe["Sex"] == "Female") & (dataframe["HeartDisease"] == "Yes")]["Smoking"].count())
    #print(count_sexMale, '\n', count_sexFemale)

    fig_smoking = px.histogram(dataframe, x="Smoking",
             color='HeartDisease', barmode='group',
             text_auto='.2s',
             labels={'Sex':'Sexo','Smoking':'Fumante', 'HeartDisease': 'Doença Cardíaca'},
             height=400)
    fig_smoking.update_layout(yaxis_title='Quantidade de indivíduos')
    fig_smoking.update_yaxes(showline=True, showgrid=False)
    fig_smoking.update_xaxes(categoryorder='category ascending',showline=True, showgrid=False)
    st.write(fig_smoking)

    st.markdown('### Alcool ')
    fig_Alcohol = px.histogram(dataframe, x="AlcoholDrinking",
            color='HeartDisease', barmode='group',
            text_auto='.2s',
            labels={'Sex':'Sexo','AlcoholDrinking':'Alcool', 'HeartDisease': 'Doença Cardíaca'},
            height=400)
    fig_Alcohol.update_layout(yaxis_title='Quantidade de indivíduos')
    fig_Alcohol.update_yaxes(showline=True, showgrid=False)
    fig_Alcohol.update_xaxes(categoryorder='category ascending',showline=True, showgrid=False)
    st.write(fig_Alcohol)

    st.markdown('### Hora de Dormir ')
    figsleeptime = px.histogram(dataframe, x="SleepTime", barmode='group',
             color='HeartDisease', histfunc='count', text_auto='.2s',
             labels={'SleepTime':'Horas de Sono', 'HeartDisease': 'Doença Cardíaca'},
             height=400)
    figsleeptime.update_layout(yaxis_title='Quantidade de indivíduos')
    figsleeptime.update_yaxes(showline=True, showgrid=False)
    figsleeptime.update_xaxes(categoryorder='category ascending',showline=True, showgrid=False)
    st.write(figsleeptime)

    st.markdown('### IMC ')
    dataframe['BMI'] = dataframe['BMI'].astype('float')
    dataframe.loc[dataframe['BMI'] <= 18.5, 'classificacao'] = 'MAGREZA'
    dataframe.loc[(dataframe['BMI'] >= 18.5) & (dataframe['BMI'] <= 24.9), 'classificacao'] = 'NORMAL'
    dataframe.loc[(dataframe['BMI'] >= 25.0) & (dataframe['BMI'] <= 29.9), 'classificacao'] = 'SOBREPESO'
    dataframe.loc[(dataframe['BMI'] >= 30.0) & (dataframe['BMI'] <= 39.9), 'classificacao'] = 'OBESIDADE'
    dataframe.loc[dataframe['BMI'] >= 40.0, 'classificacao'] = 'OBESIDADE GRAVE'


    count_magreza = int(
        dataframe[(dataframe["classificacao"] == "MAGREZA")]["classificacao"].count())

    count_normal = int(
        dataframe[(dataframe["classificacao"] == "NORMAL")]["classificacao"].count())

    count_obesidade = int(
        dataframe[(dataframe["classificacao"] == "OBESIDADE")]["classificacao"].count())

    count_obesidadegrave = int(
        dataframe[(dataframe["classificacao"] == "OBESIDADE GRAVE")]["classificacao"].count())

    count_sobrepeso = int(
        dataframe[(dataframe["classificacao"] == "SOBREPESO")]["classificacao"].count())
    
    placeholder = st.empty()

    with placeholder.container():

        kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

        kpi1.metric(
                label="Magreza",
                value=count_magreza,
                delta=count_magreza,
        )
        
        kpi2.metric(
                label="Normal",
                value=count_normal,
                delta=count_normal,
        )
        
        kpi3.metric(
                label="Obesidade",
                value=count_obesidade,
                delta=count_obesidade,
        )

        kpi4.metric(
                label="Obesidade Grave",
                value=count_obesidadegrave,
                delta=count_obesidadegrave,
        )

        kpi5.metric(
                label="SobrePeso",
                value=count_sobrepeso,
                delta=count_sobrepeso,
        )

    fig_bmi = px.histogram(dataframe, x='classificacao',
            y='BMI', color="HeartDisease", barmode='group',
            histfunc='count', text_auto='.2s',
            labels={'classificacao':'IMC', 'HeartDisease': 'Doença Cardíaca'},
            height=400)
    fig_bmi.update_layout(yaxis_title='Quantidade de indivíduos')
    fig_bmi.update_yaxes(showline=True, showgrid=False)
    fig_bmi.update_xaxes(categoryorder='category ascending',showline=True, showgrid=False)
    st.write(fig_bmi)

    st.markdown('### Idade ')
    figagecategory = px.histogram(dataframe, x="AgeCategory", color="HeartDisease", barmode='group',
             histfunc='count', text_auto='.2s',
             labels={'AgeCategory':'Idade', 'HeartDisease': 'Doença Cardíaca'},
             height=400)
    figagecategory.update_layout(yaxis_title='Quantidade de indivíduos')
    figagecategory.update_yaxes(showline=True, showgrid=False)
    figagecategory.update_xaxes(categoryorder='category ascending',showline=True, showgrid=False)
    st.write(figagecategory)

    #st.write('### ')
    st.subheader(f'''Com base nas análises feitas nos gráficos com a mesma quantidade de indivíduos que já tiveram e que não tiveram as doenças cardíaca
    Feita a análise sobre tabagismo entre indivíduos fumantes, mostrou-se que cerca de 16.037 casos de pessoas com doenças cardíacas, 
    enquanto que no Alcool são 1.141 casos. Outra análise feita com os dados sobre as horas de sono mostrou um índice maior para quem dorme entre as horas 6,7 e 8 horas.
    Os dados referente ao IMC Normal, Obesidade e SobrePeso mostraram-se com indíces ainda maiores. Uma análise feita com as idades mostrou que um aumento mais elevado e exponencial dos 45 anos até 74, sendo o maior a partir dos 80 anos.
    
    ''')
