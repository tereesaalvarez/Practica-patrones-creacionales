from Ejercicio2.prueba import *
from Ejercicio2.pizza import *

class MexicanaBuilder(PizzaBuilder):

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
        self._pizza.masa = 'masa fina'

    def producir_salsa(self) -> None:
        self._pizza.salsa = 'salsa picante de tomate'

    def producir_ingredientes(self) -> None:
        self._pizza.ingredientes = 'carne de res, chiles jalapeños, maíz, cebolla'

    def producir_coccion(self) -> None:
        self._pizza.coccion = 'horno de leña'

    def producir_presentacion(self) -> None:
        self._pizza.presentacion = 'pizza rectangular'

    def producir_maridaje(self) -> None:
        self._pizza.maridaje = 'cerveza mexicana'

    def producir_extras(self) -> None:
        self._pizza.extras = 'guacamole y crema agria'
