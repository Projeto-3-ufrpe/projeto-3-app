import dataframe
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from sklearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.metrics import plot_confusion_matrix, classification_report,confusion_matrix

def regressao_logistica_treinada():
    df = dataframe.Dados.dataframe
    x  = df.drop('HeartDisease', axis=1)#'AgeCategory',
    y = df['HeartDisease']
    # st.write(X)
    #Treinando o modelo
    X_train, X_test, y_train, y_test = train_test_split(x, y, train_size=0.3, random_state=42)
    logreg_pipeline = Pipeline(steps = [('scale',StandardScaler()),('LR',LogisticRegression(random_state=42))])
    logreg_pipeline.fit(x, y)
    # predictionsLR = logreg_pipeline.predict(x_test)
    return logreg_pipeline

def calculate_score_logistic_regression( x, y, x_test, y_test, matrix):
    logreg_pipeline = Pipeline(steps = [('scale',StandardScaler()),('LR',LogisticRegression(random_state=42))])
    logreg_pipeline.fit(x, y)
    predictionsLR = logreg_pipeline.predict(x_test)
    lgrmc = confusion_matrix(y_test, predictionsLR)
    logreg_cv = cross_val_score(logreg_pipeline, x, y, cv=10, scoring='f1')
    if matrix:
        matrix(lgrmc, 'Logistic Regression', logreg_cv)

def calculate_score_random_forest( x, y, x_test, y_test, matrix):
    rf_pipeline = Pipeline(steps = [('scale',StandardScaler()),('RF',RandomForestClassifier(random_state=42))])
    rf_pipeline.fit(x, y)
    predictionsRF = rf_pipeline.predict(x_test)
    rfcm = confusion_matrix(y_test, predictionsRF)
    rf_cv = cross_val_score(rf_pipeline, x, y, cv=10, scoring='f1')
    if matrix:
        matrix(rfcm, 'Random Forest', rf_cv)


def matrix(classifier, classifierName, score):
    score = score.mean()
    st.subheader('Matriz de Confusão ' + classifierName + ':')
    st.text_area(label = "Mean f1 score:", value = classifierName + " mean: " + str(score),  height = 1)

    fig = px.imshow(classifier, text_auto=True, aspect="auto", color_continuous_scale='ylgnbu',
                labels=dict(x="Valores previstos ", y="Valores reais", color="Número de casos"),
                x=['Predição negativa', 'Predição positiva'],
                y=['Negativo', 'Positivo']
            )

    fig.update_xaxes(side="bottom")
    st.plotly_chart(fig)

def algoritmos():

    df = dataframe.Dados.dataframe

    X  = df.drop('HeartDisease', axis=1)#'AgeCategory',
    y = df['HeartDisease']
    # st.write(X)
    #Treinando o modelo
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.3, random_state=42)

    #Balanceando os dados com Smote 
    # oversample = SMOTE()
    # X_train_resh, y_train_resh = oversample.fit_resample(X_train, y_train.ravel())


    calculate_score_random_forest(X_train, y_train, X_test, y_test)
    calculate_score_logistic_regression(X_train, y_train, X_test, y_test)

    st.markdown('___')
    st.markdown('# Conclusão')
    st.markdown('### Considerando que iremos trabalhar com a previsão do diagnostico de doenças, iremos dar mais valor ao algoritmo que retornar mais falsos positivos em relação aos falsos negativos.')
    st.markdown('### Na analise feita, podemos observar que o algoritmo de "RandomForest" retornou 22.747 falsos positivos enquanto o algoritmo de "Regressão Logistica" retornou 39.031 falsos positivos e levando isso em consideração fica evidente que o algoritmo maais confiavel é o de Regressão Logistica')