import pandas as pd
import matplotlib as plt
from sklearn.linear_model import LinearRegression

# Extraindo dados do Excel
df = pd.read_excel("Calibracao_Termopar.xlsx")
print(df)