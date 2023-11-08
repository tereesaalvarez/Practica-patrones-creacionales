
from Ejercicio2.Pizzas import margarita

def crear_margarita():
    director = Director()
    director.builder = MargaritaBuilder()
    director.build_full_featured_product()
    pizza = director.builder.pizza
    print(pizza.listar_caracteristicas())