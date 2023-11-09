
import csv

class CsvPizza:
    def __init__(self, filename):
        self.filename = filename
        self.fieldnames = ['pizza', 'masa', 'salsa', 'ingredientes', 'coccion', 'presentacion', 'maridaje', 'extras']
        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writeheader()

    def add_pizza(self, pizza, masa, salsa, ingredientes, coccion, presentacion, maridaje, extras):
        with open(self.filename, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writerow({'Pizza': pizza, 'Masa': masa, 'Salsa': salsa, 'Ingredientes': ingredientes, 'Cocción': coccion, 'Presentación': presentacion, '': , '': ,})
