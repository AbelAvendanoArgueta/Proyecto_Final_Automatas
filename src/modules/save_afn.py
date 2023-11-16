import json
import os
from src.modules.finite_automata import AutomataFinito

# Crear una instancia de la clase AutomataFinito
afn_for_saving = AutomataFinito()

def guardar_configuracion(automata, nombre_archivo):
    # Construir la ruta completa al archivo en la carpeta afn_predefined
    ruta_completa = os.path.join('src', 'afn_predefined', nombre_archivo)

    # Verificar si el archivo ya existe
    if os.path.exists(ruta_completa):
        # Si existe, agregar un número al nombre hasta encontrar un nombre único
        contador = 1
        while True:
            nuevo_nombre = f"{os.path.splitext(nombre_archivo)[0]}_{contador}.txt"
            nuevo_ruta = os.path.join('src', 'afn_predefined', nuevo_nombre)
            if not os.path.exists(nuevo_ruta):
                ruta_completa = nuevo_ruta
                break
            contador += 1

    configuracion = {
        'estados': list(automata.estados),
        'alfabeto': list(automata.alfabeto),
        'estado_inicial': automata.estado_inicial,
        'estados_aceptacion': list(automata.estados_aceptacion),
        'tabla_transiciones': automata.tabla_transiciones
    }

    with open(ruta_completa, 'w') as archivo:
        json.dump(configuracion, archivo)

def afn_save_init():
    # Se llama al método definir_automata para configurar el autómata
    afn_for_saving.definir_automata()

    # Luego se llama a la función guardar_configuracion para guardar la configuración
    guardar_configuracion(afn_for_saving, 'configuracion.txt')

# Ahora se puede llamar afn_save_init() para definir y guardar la configuración del autómata
