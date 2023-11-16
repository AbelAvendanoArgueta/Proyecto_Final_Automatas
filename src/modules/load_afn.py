import json
from src.modules.finite_automata import AutomataFinito

# Crear una nueva instancia de la clase AutomataFinito
afn_for_loading = AutomataFinito()

def cargar_configuracion(automata, nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        configuracion = json.load(archivo)

    automata.estados = set(configuracion['estados'])
    automata.alfabeto = set(configuracion['alfabeto'])
    automata.estado_inicial = configuracion['estado_inicial']
    automata.estados_aceptacion = set(configuracion['estados_aceptacion'])
    automata.tabla_transiciones = configuracion['tabla_transiciones']

def afn_load_init():
    # Cargar la configuración desde el archivo 'configuracion.txt'
    cargar_configuracion(afn_for_loading, 'configuracion.txt')

    # Mostrar mensajes de depuración
    afn_for_loading.debugging_messages()

    # Validar la cadena y mostrar los estados recorridos
    while True:
        cadena = input("\nIngrese una cadena o escriba 'salir' o 'exit' para finalizar: ")
        if cadena.lower() == 'salir' or cadena.lower() == 'exit':
            return True  # Indica que el usuario quiere salir del programa

        # Validar la cadena y mostrar los recorridos
        resultado, estados_recorridos = afn_for_loading.validar_cadena(cadena, afn_for_loading.estado_inicial, 0)

        if resultado:
            print("Estados recorridos:", " -> ".join(estados_recorridos), "\n")
        else:
            print("Estados recorridos:", " -> ".join(estados_recorridos), "\n")
