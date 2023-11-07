# Practica-patrones-creacionales

## Ejercicio 1

Desarrollar un programa en Python que haga uso del patrón de diseño Abstract Factory para modularizar y estandarizar el análisis de datos.

### Primero
Primero la interfaz abstracta de la fábrica

-create_product_a : crear_analisis_estadistico
-create_product_b : crear_graficas

### Segundo
Creo dos interfaces de producto que representan los tipos de producto que cada fábrica puede crear. (El producto de estadistica y el producto de grafica, los productos son hacer_analisis y hacer_graficas)

- useful_function_a : hacer_analisis
- useful_function_b : hacer_grafica

### Tercero
Creo dos fábricas concretas (una análisis estadístico y otra gráficos). Cada una tiene que tener los métodos para crear los productos concretos.

-Producto a: crear_analisis
-Producto b: crear_grafico

Esto devuelve los productos concretos que creo ahora

### Cuarto
Crear los productos concretos.