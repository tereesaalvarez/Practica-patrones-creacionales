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


### Implementación del Patrón de Diseño Abstract Factory
El uso del patrón de diseño Abstract Factory en la implementación del programa de análisis de datos ofrece diversas ventajas, proporcionando modularidad, flexibilidad y mantenibilidad al sistema. A continuación, se detallan algunas de las principales ventajas:

1. **Modularidad y Estandarización**:
    - El patrón Abstract Factory permite organizar el código en módulos y clases que representan familias de productos relacionados.
    - Facilita la estandarización de interfaces para la creación de productos, lo que simplifica la adición de nuevas implementaciones sin afectar el código existente.
2. **Separación de Responsabilidades**:
    - La separación entre las fábricas abstractas y los productos abstractos permite asignar responsabilidades específicas a cada componente.
    - Las fábricas concretas se encargan de la creación de productos concretos, y los productos concretos implementan las operaciones específicas.
3. **Escalabilidad**:
    - Se puede agregar fácilmente nuevas fábricas concretas y productos concretos sin modificar el código existente.
    - Permite extender el sistema para manejar diferentes tipos de análisis estadístico y gráficos en el futuro.
4. **Adaptabilidad a Cambios**:
    - Facilita la adaptación a cambios en los requisitos del sistema, ya que la lógica de creación de productos se encuentra encapsulada en las fábricas concretas.
    - Permite cambiar la familia completa de productos simplemente cambiando la fábrica concreta utilizada.
5. **Reusabilidad del Código**:
    - Los productos abstractos y las fábricas abstractas se pueden reutilizar en otros contextos y proyectos.
    - La implementación de nuevas fábricas y productos puede basarse en patrones ya establecidos.
6. **Facilita Pruebas Unitarias**:
    - La modularidad y la separación de responsabilidades facilitan las pruebas unitarias.
    - Permite la prueba individual de cada familia de productos y fábricas, mejorando la robustez del sistema.

En resumen, la implementación del patrón de diseño Abstract Factory mejora la estructura y mantenibilidad del código al proporcionar una manera elegante y eficiente de manejar familias de productos relacionados. Además, ofrece flexibilidad para adaptarse a cambios y escalabilidad para el crecimiento del sistema a lo largo del tiempo.


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

#### Implementación de Builder

El uso del patrón de diseño Builder en el simulador de pizzería ofrece varios beneficios en términos de flexibilidad, escalabilidad y mantenimiento del código. Aquí hay algunos de los beneficios clave:

1. **Creación Flexible de Objetos Complejos:**
    - El patrón Builder permite la construcción paso a paso de objetos complejos.
   - En el caso del simulador de pizzería, cada tipo de pizza puede construirse de manera modular y personalizada según los ingredientes seleccionados, gracias a los builders específicos para cada tipo de pizza.

3. **Separación de la Construcción y Representación:**
   - El patrón Builder separa el proceso de construcción de un objeto de su representación final.
   - Los builders (`barbacoa_builder.py`, `cuatro_quesos_builder.py`, etc.) se encargan de la construcción de las pizzas, mientras que la representación final de las pizzas se mantiene en las clases individuales (`barbacoa.py`, `cuatro_quesos.py`, etc.).

4. **Reusabilidad de Código:**
   - Los builders pueden reutilizarse para construir diferentes variantes de objetos.
   - En el simulador de pizzería, puedes reutilizar los builders para crear nuevas pizzas personalizadas o predefinidas sin tener que modificar el código existente.

5. **Escalabilidad:**
   - La aplicación es escalable, ya que puedes agregar nuevos tipos de pizzas simplemente creando nuevos builders y clases de pizza, sin afectar el código existente.
   - La estructura modular permite una fácil expansión de la funcionalidad sin necesidad de realizar cambios importantes en el código.

6. **Mantenimiento Sencillo:**
   - La separación de la construcción y representación facilita el mantenimiento del código.
   - Si hay cambios en la lógica de construcción de pizzas, solo necesitas ajustar el builder correspondiente sin afectar otras partes del sistema.

7. **Interfaz Gráfica Coherente:**
   - La implementación del patrón Builder contribuye a una interfaz gráfica coherente y fácil de entender para la creación de pizzas personalizadas o la selección de pizzas predefinidas.

En resumen, el uso del patrón Builder en el simulador de pizzería mejora la flexibilidad, mantenimiento y escalabilidad del código, proporcionando una estructura modular que facilita la creación y gestión de diferentes tipos de pizzas.

