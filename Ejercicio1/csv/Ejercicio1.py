import pandas as pd

data = pd.read_csv('Ejercicio1/csv/activaciones.csv', delimiter=';', encoding='ISO-8859-1')

columnas_eliminar = ['PRECIO','DIAS-EXCLUIDOS','DESCRIPCION','CONTENT-URL','URL-ACTIVIDAD','URL-INSTALACION','CODIGO-POSTAL-INSTALACION','COORDENADA-X','COORDENADA-Y','LATITUD','LATITUD','Unnamed: 29']

data= data.drop(columnas_eliminar, axis=1)


data.to_csv('Ejercicio1/csv/activaciones1.csv', index=False)

