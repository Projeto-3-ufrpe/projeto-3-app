import matplotlib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from dataframe import Dados
# %matplotlib inline

df = Dados.dataframe

#separar a quantidade de feature
features = len(df.columns - 1)
print(features)

# training_data = np.array(df.drop(''))



