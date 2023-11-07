import pandas as pd

data = pd.read_csv('Ejercicio1/csv/activaciones.csv', delimiter=';', encoding='ISO-8859-1')

data= data.dropna(axis=1, how='all')
data= data.fillna(0)

data.to_csv('Ejercicio1/csv/activaciones1.csv', index=False)
print(data.info())