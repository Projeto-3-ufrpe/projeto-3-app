import pandas as pd
class Dados:
    dataframe = pd.read_csv('../heart_2020_cleaned.csv')
    df_somente_com_doencas_do_coracao = dataframe.query("HeartDisease == 'Yes'")
    df_somente_sem_doencas_do_coracao = dataframe.query("HeartDisease == 'No'")