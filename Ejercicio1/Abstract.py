from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt

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
        #Histograma para la columna Larga duracion
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
        return 
 




def main(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    product_a = factory.crear_analisis_estadistico()
    product_b = factory.crear_grafico()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(EstadisticaFactory())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(GraficaFactory())