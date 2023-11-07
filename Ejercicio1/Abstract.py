from abc import ABC, abstractmethod

#Interfaces abstractas
class AbstractFactory(ABC):
    @abstractmethod
    def crear_analisis_estadistico(self):
        pass

    @abstractmethod
    def crear_graficas(self):
        pass

# Dos interfaces de producto que representan los tipos de producto que cada fabrica puede crear
class EstadisticaProduct(ABC):
    @abstractmethod
    def hacer_analisis(self):
        pass

class GraficaProduct(ABC):
    @abstractmethod
    def hacer_graficas(self):
        pass


#Dos fábricas concretas (una analisis y otra grafica)
class EstadisticaFactory(AbstractFactory): #?
    def create_estadistico(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_grafica(self) -> AbstractProductB:
        return ConcreteProductB1()

class GraficaFactory(AbstractFactory):
    def create_estadistico(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_grafica(self) -> AbstractProductB:
        return ConcreteProductB2()


#Productos concretos(no me hacen falta tantos como hay)
"""
Los productos concretos son creados por las correspondientes fábricas concretas.
"""
class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A1."


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A2."


#Productos abstractos 
class AbstractProductB(ABC):
    """
    Here's the the base interface of another product. All products can interact
    with each other, but proper interaction is possible only between products of
    the same concrete variant.
    """
    @abstractmethod
    def useful_function_b(self) -> None:
        """
        Product B is able to do its own thing...
        """
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        """
        ...but it also can collaborate with the ProductA.

        The Abstract Factory makes sure that all products it creates are of the
        same variant and thus, compatible.
        """
        pass




def client_code(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())