# Practica patrones creacionales

## Ejercicio 1

Desarrollar un programa en Python que haga uso del patrón de diseño Abstract Factory para modularizar y estandarizar el análisis de datos.

### Resumen del Programa de Análisis de Datos

Este programa desarrollado en Python utiliza el patrón de diseño Abstract Factory para modularizar y estandarizar el análisis de datos. A continuación, se describe el proceso del programa:

#### Estructura del Código

El código está organizado en clases que siguen el patrón Abstract Factory. Se definen las siguientes clases:

- **AbstractFactory:** Es una interfaz abstracta que declara métodos para crear instancias de análisis estadístico y gráficas.

- **Fábricas Concretas:** Existen dos fábricas concretas: `AnalisisNumericoFactory` y `AnalisisCategoricoFactory`. Cada una crea productos concretos relacionados con el análisis numérico y categórico, respectivamente.

- **Productos Abstractos:** `EstadisticaProduct` y `GraficaProduct` son interfaces abstractas que definen los métodos necesarios para realizar análisis estadístico y generar gráficas.

- **Productos Concretos:** Se tienen implementaciones concretas como `AnalisisNumerico`, `AnalisisCategorico`, `GraficaNumerica`, y `GraficaCategorica`. Cada uno realiza tareas específicas según el tipo de datos.

- **Función `main`:** La función principal (`main`) lee un archivo CSV llamado 'activaciones1.csv' utilizando la biblioteca pandas. Luego, utiliza las fábricas concretas para crear instancias de productos concretos y realiza análisis estadísticos y genera gráficas.

#### Ejecución del Programa

El código principal se encuentra en la función `main`, que se ejecuta cuando el script es llamado directamente. Dentro de `main`, se realiza lo siguiente:

1. Se carga el conjunto de datos desde el archivo 'activaciones1.csv' utilizando pandas.

2. Se crean fábricas concretas (`AnalisisNumericoFactory` y `AnalisisCategoricoFactory`) para análisis numérico y categórico.

3. Se utilizan las fábricas para crear instancias de productos concretos (`AnalisisNumerico`, `AnalisisCategorico`, `GraficaNumerica`, y `GraficaCategorica`).

4. Se realizan análisis estadísticos utilizando los productos concretos para datos numéricos y categóricos.

5. Se generan gráficas utilizando los productos concretos para datos numéricos y categóricos.

#### Resultados

Los resultados del análisis estadístico y las gráficas se imprimen en la consola y se guardan como archivos de imagen ('histograma.png' y 'barras.png'). Estos resultados proporcionan información útil sobre el conjunto de datos y permiten una fácil visualización de los patrones y distribuciones presentes en los datos.



## Ejercicio 2

### Simulador de Pizzería con Patrón de Diseño Builder
#### Resumen del Programa
Este programa es un simulador de pizzería que utiliza el patrón de diseño Builder para facilitar la creación y selección de pizzas personalizadas. Además, proporciona la opción de elegir entre diferentes pizzas predefinidas. La aplicación ha sido diseñada para mantener una estructura modular y escalable, destacando la implementación del patrón de diseño Builder para la construcción flexible de pizzas.

#### Estructura del Código
La organización del código tiene una estructura clara y es de la siguiente manera:

- Ejercicio2/
  - PizzaBuilder/
    - barbacoa_builder.py: Builder para la pizza Barbacoa.
    - cuatro_quesos_builder.py: Builder para la pizza Cuatro Quesos.
    - hawaiana_builder.py: Builder para la pizza Hawaiana.
    - jamony_queso_builder.py: Builder para la pizza Jamón y Queso.
    - margarita_builder.py: Builder para la pizza Margarita.
    - vegetariana_builder.py: Builder para la pizza Vegetariana.
    - personalizada_builder.py: Builder para pizzas personalizadas utilizando el patrón Builder.
    - director.py: Director que orquesta la construcción de pizzas utilizando el patrón Builder.
  - barbacoa.py, cuatro_quesos.py, ... : Clases que representan los distintos tipos de pizzas.
  - GUIpers.py: Interfaz gráfica para que los usuarios creen pizzas personalizadas.
  - GUIpizza.py: Interfaz gráfica para seleccionar pizzas existentes.
  - main.py: Punto de entrada principal que inicia la aplicación.

#### Ejecución del Programa

Ejecuta main.py para iniciar la aplicación.
La interfaz gráfica permite a los usuarios crear pizzas personalizadas o seleccionar pizzas existentes.
Se siguen las instrucciones en pantalla y selecciona las opciones deseadas.
Las pizzas creadas o seleccionadas se guardarán en archivos CSV (pizzas_personalizadas.csv y pizzas_existentes.csv).

#### Resultados
Las pizzas personalizadas se guardan en pizzas_personalizadas.csv.
Las pizzas existentes seleccionadas se guardan en pizzas_existentes.csv.

