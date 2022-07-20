import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import plotly.express as px
def pergunta1():
    
    st.title('Quais colunas do dataset causam um maior impacto para que o paciente desenvolva essas doenças?')
    dataframe = pd.read_csv('C:/Users/victo/OneDrive/Área de Trabalho/MAIN/PI3/heart_disease/heart_2020_cleaned.csv')
    st.markdown('### Inicio da análise: observação da influencia de cada coluna em possuir doença cardio vascular.')
    st.markdown('#### De começo iremos análisar as colunas que representam os hábitos dos individuos que, no caso, são sobre o consumo de cigarro ou alcool, sobre a prática de atividades fisicas e sobre o tempo de sono.')
    st.dataframe(dataframe[['Smoking', 'AlcoholDrinking', 'PhysicalActivity', 'SleepTime']].head())
    dataframe_yes = dataframe[(dataframe['HeartDisease'] == 'Yes')]
    st.markdown('##### Consumo de cigarros:')
    st.write(" 'HeartDisease'= Possuir ou não doenças cardiacas")
    fig, axes = plt.subplots()
    fig = plt.figure(figsize=(10,4), dpi=200)
    axes = sns.countplot(data=dataframe,x='Smoking', hue='HeartDisease', palette='Set1')
    st.pyplot(fig)
    fig, axes = plt.subplots()
    fig = plt.figure(figsize=(10,6), dpi=200)
    axes = sns.countplot(data=dataframe_yes, x='Smoking', palette="Greens_d",order=dataframe.value_counts(dataframe['Smoking']).iloc[:12].index)
    st.write('Em quais casos possuem mais doenças cardicas:')
    st.pyplot(fig)

    st.markdown('##### Consumo de alcool:')
    fig, axes = plt.subplots()
    fig = plt.figure(figsize=(10,4), dpi=200)
    axes = sns.countplot(data=dataframe,x='AlcoholDrinking', hue='HeartDisease', palette='Set1')
    st.pyplot(fig)
    fig, axes = plt.subplots()
    fig = plt.figure(figsize=(10,6), dpi=200)
    axes = sns.countplot(data=dataframe_yes, x='AlcoholDrinking', palette="Greens_d", order=dataframe.value_counts(dataframe['AlcoholDrinking']).iloc[:12].index)
    st.write('Em quais casos possuem mais doenças cardicas:')
    st.pyplot(fig)
    

    st.markdown('##### Prática de atividade fisica:')
    fig, axes = plt.subplots()
    fig = plt.figure(figsize=(10,4), dpi=200)
    axes = sns.countplot(data=dataframe,x='PhysicalActivity', hue='HeartDisease', palette='Set1')
    st.pyplot(fig)
    fig, axes = plt.subplots()
    fig = plt.figure(figsize=(10,6), dpi=200)
    axes = sns.countplot(data=dataframe_yes, x='PhysicalActivity', palette="Greens_d", order=dataframe.value_counts(dataframe['PhysicalActivity']).iloc[:12].index)
    st.write('Em quais casos possuem mais doenças cardicas:')
    st.pyplot(fig)

    st.markdown('##### O tempo de sono:')
    
    fig, axes = plt.subplots()
    fig = plt.figure(figsize=(10,6), dpi=200)
    axes = sns.countplot(data=dataframe, x='SleepTime', hue='HeartDisease', order=dataframe.value_counts(dataframe['SleepTime']).iloc[:12].index)
    st.pyplot(fig)

    fig, axes = plt.subplots()
    fig = plt.figure(figsize=(10,6), dpi=200)
    axes = sns.countplot(data=dataframe_yes, x='SleepTime', palette="Greens_d", order=dataframe.value_counts(dataframe['SleepTime']).iloc[:12].index)
    st.write('Em quais casos possuem mais doenças cardicas:')
    st.pyplot(fig)


    st.markdown('##### Oque se pode entender sobre a analise de cada coluna que representa os hábitos:')
    st.write(" É visivel que a maioria dos que possuem doenças cardiacas dormem 8horas por dia, praticam atividades fisicas, não consomem alcool, porém, fumam. O que nos leva a considerar que o fumo possui uma grande influencia na possibilidade de possuir uma doença cardiaca.")

    

