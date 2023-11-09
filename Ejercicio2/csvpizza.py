import tkinter as tk
from tkinter import messagebox
import csv

from PizzaBuilder import Builder, Director
from PizzaBuilder import barbacoa, cuatroquesos, hawaiana, jamonyqueso, margarita, personalizada, vegetariana

class PizzaGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Pizza Builder")

        self.menu_button = tk.Button(root, text="Seleccionar Pizza del Menú", command=self.select_menu_pizza)
        self.custom_button = tk.Button(root, text="Personalizar Pizza", command=self.customize_pizza)

        self.menu_button.pack()
        self.custom_button.pack()

    def select_menu_pizza(self):
        menu_window = tk.Toplevel(self.root)
        menu_window.title("Menú de Pizzas")

        barbacoa_button = tk.Button(menu_window, text="Barbacoa", command=lambda: self.build_and_save_pizza(barbacoa.BarbacoaBuilder()))
        cuatro_quesos_button = tk.Button(menu_window, text="Cuatro Quesos", command=lambda: self.build_and_save_pizza(cuatroquesos.CuatroQuesosBuilder()))
        hawaiana_button = tk.Button(menu_window, text="Hawaiana", command=lambda: self.build_and_save_pizza(hawaiana.HawaianaBuilder()))
        jamon_y_queso_button = tk.Button(menu_window, text="Jamón y Queso", command=lambda: self.build_and_save_pizza(jamonyqueso.JamonYQuesoBuilder()))
        margarita_button = tk.Button(menu_window, text="Margarita", command=lambda: self.build_and_save_pizza(margarita.MargaritaBuilder()))
        vegetariana_button = tk.Button(menu_window, text="Vegetariana", command=lambda: self.build_and_save_pizza(vegetariana.VegetarianaBuilder()))

        barbacoa_button.pack()
        cuatro_quesos_button.pack()
        hawaiana_button.pack()
        jamon_y_queso_button.pack()
        margarita_button.pack()
        vegetariana_button.pack()

    def customize_pizza(self):
        customization_window = tk.Toplevel(self.root)
        customization_window.title("Personalizar Pizza")

        builder = personalizada.PersonalizadaBuilder()
        director = Director.Director()
        director.builder = builder

        self.build_pizza_gui(customization_window, director)

    def build_pizza_gui(self, window, director):
        director.build_full_featured_product()

        finish_button = tk.Button(window, text="Finalizar", command=lambda: self.build_and_save_pizza(director.builder))
        finish_button.pack()

    def build_and_save_pizza(self, builder):
        builder.reset()
        director = Director.Director()
        director.builder = builder
        director.build_full_featured_product()

        pizza = builder.pizza
        pizza.list_parts()

        self.save_to_csv(pizza.parts)

    def save_to_csv(self, pizza_parts):
        with open('pizzas.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(pizza_parts)
            messagebox.showinfo("Éxito", "Pizza guardada en pizzas.csv")


if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaGUI(root)
    root.mainloop()
