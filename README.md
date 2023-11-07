# Practica-patrones-creacionales

## Ejercicio 1

Desarrollar un programa en Python que haga uso del patrón de diseño Abstract Factory para modularizar y estandarizar el análisis de datos.

### Primero
Primero la interfaz abstracta de la fábrica

### Segundo
Creo dos interfaces de producto que representan los tipos de producto que cada fábrica puede crear. (El producto de estadistica y el producto de grafica, los productos son hacer_analisis y hacer_graficas)

### Tercero
Creo dos fábricas concretas (una análisis estadístico y otra gráficos). Cada una tiene que tener los métodos para crear los productos concretos.

-Producto a: crear_analisis
-Producto b: crear_grafico

Esto devuelve los productos concretos que creo ahora

### Cuarto
Crear los productos concretos.