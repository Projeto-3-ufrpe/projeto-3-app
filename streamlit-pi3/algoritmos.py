import dataframe
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split,cross_val_score

def bar_plotly(df,titulo):
    fig1 = px.bar(df, x="HeartDisease", y="qtd_HeartDisease", color="HeartDisease", title=titulo, labels={ 'qtd_HeartDisease': 'Quantidade de casos', 'HeartDisease': 'Ocorrência de doenças cardíacas', 'no_HeartDisease': 'Não', 'yes_HeartDisease': 'Sim' },text_auto=True,color_discrete_map={'some_group': 'red','some_other_group': 'green'})
    fig1.update_yaxes(showline=True, showgrid=False)
    fig1.update_xaxes(categoryorder='category ascending',showline=True, showgrid=False)
    return st.plotly_chart(fig1,use_container_width=True)

def algoritmos():
    st.title('Algoritmos')

    df = dataframe.Dados.dataframe

    st.write(df)

    #Alterando as variáveis do tipo str para numéricos
    #df['HeartDisease'] = df['HeartDisease'].replace({'Yes':1,'No':0}).astype(np.uint8)
    #df['Smoking'] = df['Smoking'].replace({'Yes':1,'No':0}).astype(np.uint8)
    #df['AlcoholDrinking'] = df['AlcoholDrinking'].replace({'Yes':1,'No':0}).astype(np.uint8)
    #df['Stroke'] = df['Stroke'].replace({'Yes':1,'No':0}).astype(np.uint8)
    #df['DiffWalking'] = df['DiffWalking'].replace({'Yes':1,'No':0}).astype(np.uint8)
    #df['Sex'] = df['Sex'].replace({'Male':0,'Female':1}).astype(np.uint8)
    #df['Race'] = df['Race'].replace({'American Indian/Alaskan Native':0,'Asian':1,'Black':2,'Hispanic':3,'Other':4,'White':5}).astype(np.uint8)
    #df['GenHealth'] = df['GenHealth'].replace({'Excellent':0,'Fair':1,'Good':2,'Poor':3,'Very good':4}).astype(np.uint8)
    #df['Diabetic'] = df['Diabetic'].replace({'Yes':1,'Yes (during pregnancy)':1,'No':0,'No, borderline diabetes':0}).astype(np.uint8)
    #df['PhysicalActivity'] = df['PhysicalActivity'].replace({'Yes':1,'No':0}).astype(np.uint8)
    #df['Asthma'] = df['Asthma'].replace({'Yes':1,'No':0}).astype(np.uint8)
    #df['KidneyDisease'] = df['KidneyDisease'].replace({'Yes':1,'No':0}).astype(np.uint8)
    #df['SkinCancer'] = df['SkinCancer'].replace({'Yes':1,'No':0}).astype(np.uint8)

    #definindo todas as variavéis 
    X  = df[['Smoking','AlcoholDrinking','Stroke','DiffWalking','Sex','Asthma','Diabetic','KidneyDisease','SkinCancer','BMI']]#'AgeCategory',
    y = df['HeartDisease']

    #Treinando o modelo
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.3, random_state=42)

    #Balanceando os dados com Smote 
    oversample = SMOTE()
    X_train_resh, y_train_resh = oversample.fit_resample(X_train, y_train.ravel())

    #criando um novo dataframe com os dados balanceados
    df_balanceado = pd.DataFrame(y_train_resh,columns=['HeartDisease'])

    #montando o daframe para exibição
    depois_balanceamento=df_balanceado.groupby("HeartDisease")["HeartDisease"].count().reset_index(name='qtd_HeartDisease')
    antes_balanceamento=df.groupby("HeartDisease")["HeartDisease"].count().reset_index(name='qtd_HeartDisease')
    antes_balanceamento['HeartDisease'] = antes_balanceamento['HeartDisease'].replace({1:'Sim',0:'Não'}).astype(str)
    depois_balanceamento['HeartDisease'] = antes_balanceamento['HeartDisease'].replace({1:'Sim',0:'Não'}).astype(str)

    st.text_area(label='Dados não balanceados.', value='Observando o gráfico abaixo podemos notar que o número de casos confirmados de doenças cardácas é muito menor do que os casos não confirmados, dessa maneira seria difícil encontrar um modelo que trouxesse um resultado satisfatório.', height=100)
    bar_plotly(antes_balanceamento, "Pré-Balanceamento")
    #fig1 = px.bar(antes_balanceamento, x="HeartDisease", y="qtd_HeartDisease", color="HeartDisease", title="Antes do balanceamento", labels={ 'qtd_HeartDisease': 'Quantidade de ocorrências', 'HeartDisease': 'Ocorrência de doenças cardíacas', 'no_HeartDisease': 'Não', 'yes_HeartDisease': 'Sim' },text_auto=True,color_discrete_map={'some_group': 'red','some_other_group': 'green'})
    #fig1.update_yaxes(showline=True, showgrid=False)
    #fig1.update_xaxes(categoryorder='category ascending',showline=True, showgrid=False)
    #st.plotly_chart(fig1,use_container_width=True)

    st.text_area(label='Dados  balanceados.', value='Foi utilizado o SMOTE(Synthetic Minority Oversampling Technique) para balancear os dados e assim obter melhores resultados. Como o número de casos positivos é muito menor  do que os de casos negativos, o SMOTE foi ideal para esse balanceamento, já que ele ira preencher com mais casos positivos  nosso dataframe', height=150)
    bar_plotly(depois_balanceamento,'Pós-Balanceamento')
    #fig2 = px.bar(depois_balanceamento, x="HeartDisease", y="qtd_HeartDisease", color="HeartDisease", title="Depois do balanceamento", labels={ 'qtd_HeartDisease': 'Quantidade de ocorrências', 'HeartDisease': 'Ocorrência de doenças cardíacas', 'no_HeartDisease': 'Não', 'yes_HeartDisease': 'Sim' },text_auto=True,color_discrete_map={'some_group': 'red','some_other_group': 'green'})
    #fig2.update_yaxes(showline=True, showgrid=False)
    #fig2.update_xaxes(categoryorder='category ascending',showline=True, showgrid=False)
    #st.plotly_chart(fig2,use_container_width=True)