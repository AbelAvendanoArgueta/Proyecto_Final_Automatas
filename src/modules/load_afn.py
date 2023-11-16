import json
import os
from src.modules.finite_automata import AutomataFinito

# Crear una nueva instancia de la clase AutomataFinito
afn_for_loading = AutomataFinito()

def cargar_configuracion(automata, nombre_archivo):
    # Listar todas las configuraciones disponibles en la carpeta 'afn_predefined'
    configuraciones_disponibles = [f for f in os.listdir('src/afn_predefined') if f.endswith('.txt')]

    # Verificar si hay configuraciones disponibles
    if not configuraciones_disponibles:
        print("\n\t\tNo hay configuraciones disponibles en la carpeta 'afn_predefined'.")
        return

    # Mostrar las configuraciones disponibles al usuario
    print("\n\t\tConfiguraciones disponibles:")
    for i, configuracion in enumerate(configuraciones_disponibles, start=1):
        print(f"\t\t{i}. {configuracion}")

    # Permitir al usuario seleccionar una configuración
    while True:
        try:
            seleccion = int(input("\n\t\tSeleccione el número de la configuración a cargar: "))
            if 1 <= seleccion <= len(configuraciones_disponibles):
                nombre_archivo = configuraciones_disponibles[seleccion - 1]
                break
            else:
                print("Selección no válida. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    # Construir la ruta completa al archivo seleccionado
    ruta_completa = os.path.join('src', 'afn_predefined', nombre_archivo)

    # Cargar la configuración desde el archivo seleccionado
    with open(ruta_completa, 'r') as archivo:
        configuracion = json.load(archivo)

    automata.estados = set(configuracion['estados'])
    automata.alfabeto = set(configuracion['alfabeto'])
    automata.estado_inicial = configuracion['estado_inicial']
    automata.estados_aceptacion = set(configuracion['estados_aceptacion'])
    automata.tabla_transiciones = configuracion['tabla_transiciones']

def afn_load_init():

    # Cargar la configuración desde la carpeta 'afn_predefined'
    cargar_configuracion(afn_for_loading, 'configuracion.txt')

    # Validar la cadena y mostrar los estados recorridos
    while True:
        cadena = input("\nIngrese una cadena o escriba 'solucion' \nsi desea ver la tabla de transiciones \n\n'salir' o 'exit' para finalizar: ")
        if cadena.lower() == 'salir' or cadena.lower() == 'exit':
            return True  # Indica que el usuario quiere salir del programa
        elif cadena.lower() == 'solucion': 
            afn_for_loading.imprimir_tabla_transiciones() # Mostrar tabla de transiciones
        
        # Validar la cadena y mostrar los recorridos
        resultado, estados_recorridos = afn_for_loading.validar_cadena(cadena, afn_for_loading.estado_inicial, 0)

        if resultado:
            print("Estados recorridos:", " -> ".join(estados_recorridos), "\n")
        else:
            print("Estados recorridos:", " -> ".join(estados_recorridos), "\n")
