import matplotlib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from dataframe import Dados
#biblioteca que auxilia padronizar os dados para aplicar a regressão logística
import sklearn.preprocessing as sk

#Criar x0's com valores iguais a 1 (?)
def insert_notes(X):
    ones = np.ones([X.shape[0], 1])
    return np.concatenate((ones, X), axis=1)

#função que faz que a nossa regressão possa ser aplicada em um problema de classificação / minuto 2:54 do video
#https://www.youtube.com/watch?v=yV9ipYEtvnM
def sigmoid(z):
    pass

    

df = Dados.dataframe_somente_com_colunas_numericas
#pegar o número da coluna booleana, no nosso caso, SkinCancer
features = len(df.columns) - 1
# training_data = os dados em formato de lista sem a coluna passada no parâmetro de df.drop()
training_data = np.array(df.drop('SkinCancer', axis=1))
# target_variable = pegando os dados da coluna target em forma de lista também
target_variable = df.iloc[:,features:features + 1 ].values
#precisamos somente de valores número em todas as colunas, fazer esse tratamento da média
media_valores = training_data.mean(axis=0)
desvio_padrao = training_data.std(axis=0)
#padronizar os dados para aplicação da regressão logística
scaler = sk.StandardScaler()
scaler.fit(training_data)
training_data = scaler.transform(training_data)
#criando uma matriz do tamanho de uma linha da tabela com valores aleatórios entre 0 e 1
linha_w = np.random.rand(1, features+1)
print(linha_w)









