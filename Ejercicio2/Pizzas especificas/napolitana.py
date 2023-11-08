from Ejercicio2.prueba import *
from Ejercicio2.pizza import *

class NapolitanaBuilder(PizzaBuilder):

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
        self._pizza.salsa = 'salsa de tomate'

    def producir_ingredientes(self) -> None:
        self._pizza.ingredientes = 'tomate fresco, anchoas, aceitunas negras, ajo, orégano'

    def producir_coccion(self) -> None:
        self._pizza.coccion = 'horno de leña'

    def producir_presentacion(self) -> None:
        self._pizza.presentacion = 'pizza circular'

    def producir_maridaje(self) -> None:
        self._pizza.maridaje = 'vino tinto italiano'

    def producir_extras(self) -> None:
        self._pizza.extras = 'aceite de oliva extra virgen'
