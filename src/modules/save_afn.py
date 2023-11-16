import json
from src.modules.finite_automata import AutomataFinito

# Crear una instancia de la clase AutomataFinito
afn_for_saving = AutomataFinito()

def guardar_configuracion(automata, nombre_archivo):
    configuracion = {
        'estados': list(automata.estados),
        'alfabeto': list(automata.alfabeto),
        'estado_inicial': automata.estado_inicial,
        'estados_aceptacion': list(automata.estados_aceptacion),
        'tabla_transiciones': automata.tabla_transiciones
    }

    with open(nombre_archivo, 'w') as archivo:
        json.dump(configuracion, archivo)

def afn_save_init():
    # Se llama al método definir_automata para configurar el autómata
    afn_for_saving.definir_automata()

    # Luego se llama a la función guardar_configuracion para guardar la configuración
    guardar_configuracion(afn_for_saving, 'configuracion.txt')

# Ahora puedes llamar afn_save_init() para definir y guardar la configuración del autómata
