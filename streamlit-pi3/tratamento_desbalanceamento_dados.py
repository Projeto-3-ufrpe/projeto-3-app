import streamlit as st
import dataframe
import sklearn
import numpy as np
from sklearn import model_selection, dummy, metrics
def desbalanceamento_dados():
    st.title("A Partir dos dados abaixo podemos notar que há um desbalanceamento dos dados")
    df = dataframe.Dados.dataframe
    quantidade_dados_com_doencas_coracao = df['HeartDisease'].loc[df['HeartDisease'] == 1].count()
    quantidade_dados_sem_doencas_coracao = df['HeartDisease'].loc[df['HeartDisease'] == 0].count()
    st.subheader('# Quantidade de Dados com doenças do coração - ' + str(quantidade_dados_com_doencas_coracao))
    st.subheader('# Quantidade de Dados sem doenças do coração - ' + str(quantidade_dados_sem_doencas_coracao))
    #testando com DummyClassifier
    y = df.HeartDisease
    X = df.drop('HeartDisease', axis=1)
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.25, random_state=27)
    # DummyClassifier to predict only target 0
    st.subheader(' - Vamos usar o DummyClassifier para visualizar o desbalanceamento em uma predição "burra"')
    dummy_classifier = dummy.DummyClassifier(strategy='most_frequent').fit(X_train, y_train)
    dummy_pred = dummy_classifier.predict(X_test)
    # checking unique labels
    st.subheader('# Unique predicted labels: {}'.format(np.unique(dummy_pred)))
    # checking accuracy
    st.subheader('# Test score: {}'.format(metrics.accuracy_score(y_test, dummy_pred)))

