# Proyecto de Autómatas Finitos No Deterministas (AFN)

## Descripción del Proyecto

Este proyecto implementa un sistema para definir, guardar, cargar y validar configuraciones de Autómatas Finitos No Deterministas (AFN). Permite a los usuarios interactuar con el autómata, ingresando cadenas para su validación y explorando las transiciones del autómata.

## Universidad

- **Universidad Panamericana de Guatemala**
- **Facultad de Ingeniería y Ciencias Aplicadas**
- **Carrera de Ingeniería en Sistemas y Tecnologías de la Información y Comunicación**

## Integrantes del Equipo

- **Deneth Javier Gómez Corado** - Carné: 000127597
- **Abel Fernando Avendaño Argueta** - Carné: 000127599
- **Brayan Alexander Ríos y Ríos** - Carné: 000130200
- **Jerson Eduardo Gutiérrez Gamez** - Carné: 000126122
- **Giancarlo Josué Contreras Sandoval** - Carné: 000130757

## Funcionalidades del Programa

- **Definición de Autómata Finito No Determinista (AFN):** Los usuarios pueden definir estados, alfabeto, estado inicial, estados de aceptación y las transiciones del autómata.

- **Guardado de Configuraciones:** Permite guardar la configuración del autómata en archivos JSON para su posterior carga.

- **Carga de Configuraciones:** Los usuarios pueden cargar configuraciones predefinidas de autómatas finitos desde archivos JSON.

- **Validación de Cadenas:** Los usuarios pueden ingresar cadenas para ser validadas por el autómata, mostrando los estados recorridos.

## Estructura del Proyecto

- **`__main__.py`:** Punto de entrada principal del programa.
- **`README.md`:** Este archivo, proporcionando información sobre el proyecto.

- **`src/`:** Directorio que contiene el código fuente del proyecto.

  - **`afn_predefined/`:** Carpeta que almacena configuraciones predefinidas de autómatas finitos.

  - **`modules/`:** Carpeta que contiene los módulos del programa.

    - **`finite_automata.py`:** Definición de la clase `AutomataFinito` que representa un autómata finito.

    - **`load_afn.py`:** Implementación de la carga de configuraciones y validación de cadenas.

    - **`save_afn.py`:** Implementación del guardado de configuraciones.

    - **`main_menu.py`:** Implementación del menú principal y ejecución del programa.

## Instrucciones de Uso

1. Ejecute el archivo `__main__.py` para iniciar el programa.
2. Seleccione las opciones del menú para definir, guardar, cargar y validar configuraciones de autómatas finitos.
3. ¡Disfrute interactuando con el autómata finito!
