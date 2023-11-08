from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Interfaces abstractas
class AbstractFactory(ABC):
    @abstractmethod
    def crear_analisis_estadistico(self):
        pass

    @abstractmethod
    def crear_graficas(self):
        pass


#Dos fábricas concretas (una analisis y otra grafica)
class AnalisisNumericoFactory(AbstractFactory):
    def crear_analisis_estadistico(self):
        return AnalisisNumerico()

    def crear_graficas(self):
        return GraficaNumerica()

class AnalisisCategoricoFactory(AbstractFactory):
    def crear_analisis_estadistico(self):
        return AnalisisCategorico()

    def crear_graficas(self):
        return GraficaCategorica()


#PRODUCTOS ABSTRACTOS
class EstadisticaProduct(ABC):
    @abstractmethod
    def hacer_analisis(self):
        pass

class GraficaProduct(ABC):
    @abstractmethod
    def hacer_graficas(self):
        pass

#PRODUCTOS CONCRETOS
class AnalisisNumerico(EstadisticaProduct):

    def hacer_analisis(self,data) -> str:
        columnas_numericas = data.select_dtypes(include=['int64', 'float64'])
        resultado = {
            'Media': columnas_numericas.mean(),
            'Moda': columnas_numericas.mode().iloc[0],
            'Mediana': columnas_numericas.median()
        }
        return resultado

class AnalisisCategorico(EstadisticaProduct):

    def hacer_analisis(self,data) -> str:
        columnas_categoricas = data.select_dtypes(include=['object'])
        resultado = {
            'Moda': columnas_categoricas.mode().iloc[0]
        }
        return resultado


class GraficaNumerica(GraficaProduct):
    def hacer_graficas(self,data) -> str:
        #Histograma para la columna numerica Larga duracion
        plt.figure(figsize=(10,6))
        plt.histplot(data, x='LARGA-DURACION', kde=True)
        plt.title('Histograma de Larga duracion')
        plt.xlabel('LARGA-DURACIÓN')
        plt.ylabel('Frecuencia')
        #Los guardo en vez de que se muestren
        plt.savefig('Ejercicio1/imagenes/histograma.png')
        return 

class GraficaCategorica(GraficaProduct):
    def hacer_graficas(self,data) -> str:
        #Grafico de barras para la columna Dias semana
        plt.figure(figsize=(10,6))
        sns.countplot(data=data, x='DIAS-SEMANA', order=data['DIAS-SEMANA'].value_counts().index)
        plt.title('Grafico de barras de dias semana')
        plt.xlabel('DIAS-SEMANA')
        plt.ylabel('Frecuencia')
        #Los guardo en vez de que se muestren
        plt.savefig('Ejercicio1/imagenes/barras.png')
        return 
 




def main(factory: AbstractFactory) -> None:
    data= pd.read_csv('Ejercicio1/csv/activaciones1.csv')
    #crear fabrica de analisis numerico
    fabrica_numerica = AnalisisNumericoFactory()

    #analisis estadistico de las columas numericas
    analisis_numerico = fabrica_numerica.crear_analisis_estadistico()
    resultado_numerico = analisis_numerico.hacer_analisis(data)
    print(resultado_numerico)

    #crear fabrica de analisis categorico
    fabrica_categorica = AnalisisCategoricoFactory()

    #analisis estadistico de las columas categoricas
    analisis_categorico = fabrica_categorica.crear_analisis_estadistico()
    resultado_categorico = analisis_categorico.hacer_analisis(data)
    print(resultado_categorico)

    #graficas
    histograma = fabrica_numerica.crear_graficas()
    histograma.hacer_graficas(data)

    barras = fabrica_categorica.crear_graficas()
    barras.hacer_graficas(data)

if __name__ == "__main__":
    main()