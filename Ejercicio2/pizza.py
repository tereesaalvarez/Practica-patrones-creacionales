#clase pizza para represetnar el producto final

class Pizza():

    def __init__(self) -> None:
        self.masa = ''
        self.salsa = ''
        self.ingredientes = ''
        self.coccion = ''
        self.presentacion = ''
        self.maridaje = ''
        self.extras = ''


    def partes(self) -> None:
        print(f"Partes de la pizza: {self.masa}, {self.salsa}, {self.ingredientes}, {self.coccion}, {self.presentacion}, {self.maridaje}, {self.extras}", end="")
