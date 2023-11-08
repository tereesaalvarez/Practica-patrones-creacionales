from abc import ABC, abstractmethod
import pandas as pd

#Interfaces abstractas
class AbstractFactory(ABC):
    @abstractmethod
    def crear_analisis_estadistico(self):
        pass

    @abstractmethod
    def crear_graficas(self):
        pass


#Dos fábricas concretas (una analisis y otra grafica)
class EstadisticaFactory(AbstractFactory): #?
    def crear_analisis_estadistico(self):
        return MediaModaMediana()

    def crear_graficas(self):
        return None

class GraficaFactory(AbstractFactory):
    def crear_analisis_estadistico(self):
        return None

    def crear_graficas(self):
        return RepresentacionGraficas()


#PRIMER PRODUCTO ABSTRACTO
class EstadisticaProduct(ABC):
    @abstractmethod
    def hacer_analisis(self):
        pass

#Primer producto concreto para primer producto abstracto
class MediaModaMediana(EstadisticaProduct):
    def __init__(self):
        self.data = pd.read_csv('Ejercicio1/csv/activaciones1.csv')
        self.media = self.data.media()
        self.moda = self.data.moda()
        self.mediana = self.data.mediana()
        
    def hacer_analisis(self) -> str:

        pass


#SEGUNDO PRODUCTO ABSTRACTO
class GraficaProduct(ABC):
    @abstractmethod
    def hacer_graficas(self):
        pass

#Primer producto concreto para primer producto abstracto
class RepresentacionGraficas(GraficaProduct):
    def hacer_graficas(self) -> str:
        return "The result of the product A2."


 




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