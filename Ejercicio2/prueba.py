from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class PizzaBuilder(ABC):

    @property
    @abstractmethod
    def pizza(self) -> None:
        pass

    @abstractmethod
    def producir_masa(self) -> None:
        pass

    @abstractmethod
    def producir_salsa(self) -> None:
        pass

    @abstractmethod
    def producir_ingredientes(self) -> None:
        pass

    @abstractmethod
    def producir_coccion(self) -> None:
        pass

    @abstractmethod
    def producir_presentacion(self) -> None:
        pass

    @abstractmethod
    def producir_maridaje(self) -> None:
        pass

    @abstractmethod
    def producir_extras(self) -> None:
        pass






if __name__ == "__main__":
   

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()