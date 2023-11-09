# main.py
from GUIpers import PizzaPersonalizadaGUI
from GUIpizza import PizzaExistenteGUI
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()

    # Interfaz para pizza personalizada
    personalizada_gui = PizzaPersonalizadaGUI(root)

    # Interfaz para pizza existente
    existente_gui = PizzaExistenteGUI(root)

    root.mainloop()


