from Builder import *
from Ejercicio2.pizza import *

class CuatroQuesosBuilder(PizzaBuilder):

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
        self._pizza.ingredientes = 'queso azul, queso brie, queso de cabra, queso mozzarella'

    def producir_coccion(self) -> None:
        self._pizza.coccion = 'horno de piedra'

    def producir_presentacion(self) -> None:
        self._pizza.presentacion = 'pizza circular'

    def producir_maridaje(self) -> None:
        self._pizza.maridaje = 'vino tinto'

    def producir_extras(self) -> None:
        self._pizza.extras = 'nuez picada'
