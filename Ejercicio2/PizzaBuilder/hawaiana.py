from __future__ import annotations
from typing import Any
from Builder import PizzaBuilder
from abc import ABC, abstractmethod

#deberia de estar prohibida
class HawaianaBuilder(PizzaBuilder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._pizza = Hawaiana()

    @property
    def pizza(self) -> Hawaiana:
        pizza = self._pizza
        self.reset()
        return pizza

    def producir_masa(self) -> None:
        self._pizza.masa = 'masa fina'

    def producir_salsa(self) -> None:
        self._pizza.salsa = 'salsa de tomate'

    def producir_ingredientes(self) -> None:
        self._pizza.ingredientes = 'jamón, piña, queso mozzarella'

    def producir_coccion(self) -> None:
        self._pizza.coccion = 'horno tradicional'

    def producir_presentacion(self) -> None:
        self._pizza.presentacion = 'pizza circular'

    def producir_maridaje(self) -> None:
        self._pizza.maridaje = 'zumo de piña'

    def producir_extras(self) -> None:
        self._pizza.extras = 'cerezas en almíbar'


class Hawaiana():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")