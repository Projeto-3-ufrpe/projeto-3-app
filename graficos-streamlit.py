import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# import plotly.express as px


with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Início", "teste")
    )
st.title('Personal Key Indicators of Heart Disease')

dataframe = pd.read_csv('C:/Users/victo/OneDrive/Área de Trabalho/MAIN/PI3/heart_disease/heart_2020_cleaned.csv')
st.dataframe(dataframe)

chart_data = pd.DataFrame(list(zip(dataframe['BMI'].tolist(),dataframe['PhysicalHealth'].tolist(),dataframe['MentalHealth'].tolist())),
columns = ['Body Mass Index (BMI)','PhysicalHealth','MentalHealth'])
range_chart = st.slider('Quantidade de dados no gráfico', 0, 300, 30)
st.title('Informações do DataFrame')

# fig, x = plt.subplots()
# x.hist(data=dataframe, y='SleepTime', x='HeartDisease')

# st.pyplot(fig)

st.area_chart(chart_data.head(range_chart))

# fig = px.bar(dataframe, x='bmi', y='heartdisease')
# st.write(fig)