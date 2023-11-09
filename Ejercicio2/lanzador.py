from csvpizza import CsvPizza
import tkinter as tk


def crear_interfaz():
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Pizzería")

    # Crear el menú desplegable de pizzas predefinidas
    opciones_pizzas = ["Margarita", "Pepperoni", "Hawaiana"]
    pizza_seleccionada = tk.StringVar(ventana)
    pizza_seleccionada.set(opciones_pizzas[0])
    pizza_menu = tk.OptionMenu(ventana, pizza_seleccionada, *opciones_pizzas)
    pizza_menu.pack()

    # Crear la sección para crear una pizza personalizada
    crear_pizza_label = tk.Label(ventana, text="Crear tu propia pizza")
    crear_pizza_label.pack()

    nombre_label = tk.Label(ventana, text="Nombre:")
    nombre_label.pack()
    nombre_entry = tk.Entry(ventana)
    nombre_entry.pack()

    ingredientes_label = tk.Label(ventana, text="Ingredientes:")
    ingredientes_label.pack()
    ingredientes_entry = tk.Entry(ventana)
    ingredientes_entry.pack()

    precio_label = tk.Label(ventana, text="Precio:")
    precio_label.pack()
    precio_entry = tk.Entry(ventana)
    precio_entry.pack()

    guardar_button = tk.Button(ventana, text="Guardar pizza", command=CsvPizza.añadir_pizza)
    guardar_button.pack()

    # Iniciar el bucle de eventos de la ventana
    ventana.mainloop()

if __name__ == "__main__":
    crear_interfaz()






