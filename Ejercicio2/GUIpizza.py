import tkinter as tk
from tkinter import messagebox
import csv

from PizzaBuilder import Builder, Director
from PizzaBuilder import barbacoa, cuatroquesos, hawaiana, jamonyqueso, margarita, personalizada, vegetariana
from GUIpers import *


class PersonalizadaGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Personalizar Pizza")

        self.builder = personalizada.PersonalizadaBuilder()
        self.director = Director()
        self.director.builder = self.builder

        self.create_masa_section()
        self.create_salsa_section()
        self.create_ingredientes_section()
        self.create_coccion_section()
        self.create_presentacion_section()
        self.create_maridaje_section()
        self.create_extras_section()

        finish_button = tk.Button(root, text="Finalizar", command=self.finalize_pizza)
        finish_button.pack()

    def create_masa_section(self):
        masa_label = tk.Label(self.root, text="Selecciona el tipo de masa:")
        masa_label.pack()

        self.masa_var = tk.StringVar()
        masa_options = ["fina", "normal, gruesa"]
        masa_menu = tk.OptionMenu(self.root, self.masa_var, *masa_options)
        masa_menu.pack()

    def create_salsa_section(self):
        salsa_label = tk.Label(self.root, text="Selecciona el tipo de salsa:")
        salsa_label.pack()

        self.salsa_var = tk.StringVar()
        salsa_options = ["tomate", "barbacoa"]
        salsa_menu = tk.OptionMenu(self.root, self.salsa_var, *salsa_options)
        salsa_menu.pack()

    def create_ingredientes_section(self):
        ingredientes_label = tk.Label(self.root, text="Selecciona los ingredientes (fin para ninguno):")
        ingredientes_label.pack()

        self.ingredientes_text = tk.Entry(self.root)
        self.ingredientes_text.pack()

    def create_coccion_section(self):
        coccion_label = tk.Label(self.root, text="Selecciona el tipo de cocción:")
        coccion_label.pack()

        self.coccion_var = tk.StringVar()
        coccion_options = ["horno tradicional", "horno de leña", "horno de piedra"]
        coccion_menu = tk.OptionMenu(self.root, self.coccion_var, *coccion_options)
        coccion_menu.pack()

    def create_presentacion_section(self):
        presentacion_label = tk.Label(self.root, text="Selecciona el tipo de presentación:")
        presentacion_label.pack()

        self.presentacion_var = tk.StringVar()
        presentacion_options = ["pizza circular", "pizza rectangular"]
        presentacion_menu = tk.OptionMenu(self.root, self.presentacion_var, *presentacion_options)
        presentacion_menu.pack()

    def create_maridaje_section(self):
        maridaje_label = tk.Label(self.root, text="Selecciona el tipo de maridaje:")
        maridaje_label.pack()

        self.maridaje_var = tk.StringVar()
        maridaje_options = ["cerveza rubia", "vino blanco", "refresco de cola", "vino tinto"]
        maridaje_menu = tk.OptionMenu(self.root, self.maridaje_var, *maridaje_options)
        maridaje_menu.pack()

    def create_extras_section(self):
        extras_label = tk.Label(self.root, text="Selecciona los extras (fin para ninguno):")
        extras_label.pack()

        self.extras_text = tk.Entry(self.root)
        self.extras_text.pack()

    def finalize_pizza(self):
        self.builder.producir_masa(self.masa_var.get())
        self.builder.producir_salsa(self.salsa_var.get())

        ingredientes_input = self.ingredientes_text.get()
        ingredientes = ingredientes_input.split(", ")
        for ingrediente in ingredientes:
            self.builder.producir_ingredientes(ingrediente)

        self.builder.producir_coccion(self.coccion_var.get())
        self.builder.producir_presentacion(self.presentacion_var.get())
        self.builder.producir_maridaje(self.maridaje_var.get())

        extras_input = self.extras_text.get()
        extras = extras_input.split(", ")
        for extra in extras:
            self.builder.producir_extras(extra)

        self.builder.reset()
        self.director.builder = self.builder
        self.director.build_full_featured_product()

        pizza = self.builder.pizza
        pizza.list_parts()

        self.save_to_csv(pizza.parts)

    def save_to_csv(self, pizza_parts):
        with open('pizzas.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(pizza_parts)
            messagebox.showinfo("Éxito", "Pizza guardada en pizzas.csv")


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
        jamon_y_queso_button = tk.Button(menu_window, text="Jamón y Queso", command=lambda: self.build_and_save_pizza(jamonyqueso.JamonyQuesoBuilder()))
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
        personalizada_gui = PersonalizadaGUI(customization_window)

    def build_and_save_pizza(self, builder):
        builder.reset()
        director = Director()
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