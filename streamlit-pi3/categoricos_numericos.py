import dataframe
import streamlit as st
import dataframe
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pandas as pd
import numpy as np

df = dataframe.Dados.dataframe
labelEncoder = LabelEncoder()
oneHotEncoder = OneHotEncoder()


class numericos:
    labels_sex = labelEncoder.fit_transform(df.Sex)
    df['Sex'] = labels_sex
    dataframa = df
    feature_Arr = pd.get_dummies(dataframa['AgeCategory'])
    dataframa = pd.concat([dataframa, feature_Arr], axis=1)
    dataframa = dataframa.drop('AgeCategory', axis=1)
    feature_Arr = pd.get_dummies(dataframa['Race'])
    dataframa = pd.concat([dataframa, feature_Arr], axis=1)
    dataframa = dataframa.drop('Race', axis=1)
    feature_Arr = pd.get_dummies(dataframa['GenHealth'])
    dataframa = pd.concat([dataframa, feature_Arr], axis=1)
    dataframa = dataframa.drop('GenHealth', axis=1)
    dataframe_numerico = dataframa
    
def categoricos_to_numericos():
    st.markdown('# Passando atributos categorigos para numericos')
    st.markdown('___')

    st.dataframe(df.head())

    st.markdown('#### O objetivo dessa fase do processamento dos dados é converter todas as colunas que são categoricas para numericas.')
    st.markdown('#### Pra isso serão utilizados dois algoritimos.')
    st.markdown('- LabelEncoder')
    st.markdown('- OneHotEncoder')
    st.markdown('#### Basicamente, o LabelEncoder tranforma cada um das categorias em um numero enquanto o OneHotEncoder tranforma cada categoria em uma coluna. No caso do OneHotEncoder, iremos utilizar o método "get_dummies" da biblioteca Pandas, pois ela irá executar a mesma tarefa de forma mais simples.')
    
    st.markdown('___')

    st.markdown('#### Primeiramente iremos fazer a conversão com a coluna "Sex". Sexo feminino será representado pelo 0 e o masculino pelo 1.')
    labels_sex = labelEncoder.fit_transform(df.Sex)
    df['Sex'] = labels_sex
    st.dataframe(df.head())
    st.markdown('#### A coluna "SEX" foi a unica na qual foi possivel aplicar o LabelEncoder. A partir de agora iremos trabalhar com o OneHotEncode.')
    st.markdown(" ")
    st.markdown('#### Agora iremos adicionar o "dummies" a categoria "AgeCategory".')
    dataframa = df
    feature_Arr = pd.get_dummies(dataframa['AgeCategory'])
    dataframa = pd.concat([dataframa, feature_Arr], axis=1)
    dataframa = dataframa.drop('AgeCategory', axis=1)
    st.dataframe(dataframa.head())
    print(feature_Arr)
    st.markdown(" ")
    st.markdown('#### "Dummies" para a categoria "Race".')
    feature_Arr = pd.get_dummies(dataframa['Race'])
    dataframa = pd.concat([dataframa, feature_Arr], axis=1)
    dataframa = dataframa.drop('Race', axis=1)
    st.dataframe(dataframa.head())
    st.markdown('#### Após aplicar o "Dummies" para a categoria "GenHealth" nós temos o nosso conjunto de dados final com todas as colunas agora numericas.')
    feature_Arr = pd.get_dummies(dataframa['GenHealth'])
    dataframa = pd.concat([dataframa, feature_Arr], axis=1)
    dataframa = dataframa.drop('GenHealth', axis=1)
    st.dataframe(dataframa.head())

