from __future__ import annotations
from typing import Any
from Builder import PizzaBuilder
from abc import ABC, abstractmethod

from __future__ import annotations
from typing import Any
from Builder import PizzaBuilder
from abc import ABC, abstractmethod

class PersonalizadaBuilder(PizzaBuilder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._pizza = Personalizada()

    @property
    def pizza(self) -> Personalizada:
        pizza = self._pizza
        self.reset()
        return pizza

    def producir_masa(self) -> None:
        masa = input("Elige el tipo de masa (fina, normal, gruesa)")
        self._pizza.masa = 'masa fina'

    def producir_salsa(self) -> None:
        self._pizza.salsa = 'salsa de tomate'

    def producir_ingredientes(self) -> None:
        self._pizza.ingredientes = 'tomate, champiñones, pimientos, cebolla, aceitunas negras'

    def producir_coccion(self) -> None:
        self._pizza.coccion = 'horno tradicional'

    def producir_presentacion(self) -> None:
        self._pizza.presentacion = 'pizza circular'

    def producir_maridaje(self) -> None:
        self._pizza.maridaje = 'vino blanco o refresco'

    def producir_extras(self) -> None:
        self._pizza.extras = 'albahaca fresca y queso parmesano'

class Personalizada():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")