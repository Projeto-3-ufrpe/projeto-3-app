import pandas as pd
import numpy as np


dataframe_nao_numerico = pd.read_parquet('../heart_2020_cleaned.parquet')
def tratamento_csv(dataframe,list_columns):
    #nas colunas booleanas trocar 'sim' e 'não' por 0 e 1
    for column in list_columns:
        if column == 'Diabetic':
            dataframe[column] = np.where(dataframe[column] == 'No, borderline diabetes', 0, dataframe[column])
            dataframe[column] = np.where(dataframe[column] == 'Yes (during pregnancy)', 1, dataframe[column])
        dataframe[column] = np.where(dataframe[column] == 'Yes', 1, dataframe[column])
        dataframe[column] = np.where(dataframe[column] == 'No', 0, dataframe[column])
        dataframe[f'{column}'] = pd.to_numeric(dataframe[f'{column}'])
    return dataframe

class Dados:
    dataframe = pd.read_parquet('../heart_2020_cleaned.parquet')
    dataframe = tratamento_csv(dataframe, ['HeartDisease', 'Smoking', 'AlcoholDrinking', 'KidneyDisease', 'SkinCancer', 'Asthma', 'Diabetic', 'PhysicalActivity','DiffWalking','Stroke'])
    dataframe_somente_com_colunas_numericas = dataframe.drop(columns=['AgeCategory','GenHealth', 'Race','Sex', ])
    dataframe['SkinCancer'] = np.where(dataframe['SkinCancer'] == 'Yes', 1, dataframe['SkinCancer'])
    dataframe['SkinCancer'] = np.where(dataframe['SkinCancer'] == 'No', 0, dataframe['SkinCancer'])
    df_somente_com_doencas_do_coracao = dataframe.query("HeartDisease == 'Yes'")
    df_somente_sem_doencas_do_coracao = dataframe.query("HeartDisease == 'No'")
    dataframe['Sex'] = dataframe['Sex'].replace({'Male':0,'Female':1}).astype(np.uint8)
    dataframe['GenHealth'] = dataframe['GenHealth'].replace({'Excellent':0,'Fair':1,'Good':2,'Poor':3,'Very good':4}).astype(np.uint8)
    dataframe['Race'] = dataframe['Race'].replace({'American Indian/Alaskan Native':0,'Asian':1,'Black':2,'Hispanic':3,'Other':4,'White':5}).astype(np.uint8)


