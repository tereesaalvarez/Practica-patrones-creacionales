from __future__ import annotations
from typing import Any
from Builder import PizzaBuilder
from abc import ABC, abstractmethod

class JamonyQuesoBuilder(PizzaBuilder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._pizza = Jamonyqueso()

    @property
    def pizza(self) -> Jamonyqueso:
        pizza = self._pizza
        self.reset()
        return pizza

    def producir_masa(self) -> None:
        self._pizza.masa = 'masa fina'

    def producir_salsa(self) -> None:
        self._pizza.salsa = 'salsa de tomate'

    def producir_ingredientes(self) -> None:
        self._pizza.ingredientes = 'jamón, queso mozzarella'

    def producir_coccion(self) -> None:
        self._pizza.coccion = 'horno tradicional'

    def producir_presentacion(self) -> None:
        self._pizza.presentacion = 'pizza circular'

    def producir_maridaje(self) -> None:
        self._pizza.maridaje = 'vino blanco'

    def producir_extras(self) -> None:
        self._pizza.extras = 'aceitunas negras'

class Jamonyqueso():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")