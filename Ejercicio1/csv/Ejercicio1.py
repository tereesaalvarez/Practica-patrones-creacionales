import pandas as pd

data = pd.read_csv('Ejercicio1/csv/activaciones.csv', delimiter=';', encoding='ISO-8859-1')

data= data.dropna(axis=1, how='all')
data = data.dropna(thresh=len(data.columns) - 4)


data.to_csv('Ejercicio1/csv/activaciones1.csv', index=False)

