from Builder import *


class BarbacoaBuilder(PizzaBuilder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._pizza = Pizza()

    @property
    def pizza(self) -> Pizza:
        pizza = self._pizza
        self.reset()
        return pizza

    def producir_masa(self) -> None:
        self._pizza.masa = 'masa gruesa'

    def producir_salsa(self) -> None:
        self._pizza.salsa = 'salsa barbacoa'

    def producir_ingredientes(self) -> None:
        self._pizza.ingredientes = 'pollo, cebolla, maíz'

    def producir_coccion(self) -> None:
        self._pizza.coccion = 'horno de leña'

    def producir_presentacion(self) -> None:
        self._pizza.presentacion = 'pizza rectangular'

    def producir_maridaje(self) -> None:
        self._pizza.maridaje = 'refresco de cola'

    def producir_extras(self) -> None:
        self._pizza.extras = 'salsa barbacoa adicional'


class Product1():
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")