import os
from src.modules.finite_automata import AutomataFinito

ascii_art = """
 █████╗ ██╗   ██╗████████╗ ██████╗ ███╗   ███╗ █████╗ ████████╗ █████╗     ███████╗██╗███╗   ██╗██╗████████╗ ██████╗ 
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗████╗ ████║██╔══██╗╚══██╔══╝██╔══██╗    ██╔════╝██║████╗  ██║██║╚══██╔══╝██╔═══██╗
███████║██║   ██║   ██║   ██║   ██║██╔████╔██║███████║   ██║   ███████║    █████╗  ██║██╔██╗ ██║██║   ██║   ██║   ██║
██╔══██║██║   ██║   ██║   ██║   ██║██║╚██╔╝██║██╔══██║   ██║   ██╔══██║    ██╔══╝  ██║██║╚██╗██║██║   ██║   ██║   ██║
██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║    ██║     ██║██║ ╚████║██║   ██║   ╚██████╔╝
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝    ╚═════╝ 
                                                                                                                                                                                                                                                             
"""

def print_header(text):
    total_columns = 142  # Número total de caracteres, incluyendo espacios en blanco
    terminal_size = os.get_terminal_size().columns

    if terminal_size < total_columns:
        print("La terminal es demasiado pequeña para centrar el texto correctamente.")
        return

    padding = (terminal_size - total_columns) // 2
    header = ' ' * padding + text + ' ' * padding
    print(header)  # Asegurarse de que no se exceda el tamaño de la terminal

def imprimir_menu():
    while True:
        print_header("UNIVERSIDAD PANAMERICANA DE GUATEMALA")
        print_header("Facultad de Ingeniería y Ciencias Aplicadas")
        print_header("Carrera de Ingeniería en Sistemas y Tecnologías de la Información y Comunicación")
        print_header("Abel Fernando Avendaño Argueta 000127599")
        print_header("Deneth Javier Gómez Corado 000127597")
        print_header("Brayan Alexander Ríos y Ríos 000130200")
        print_header(ascii_art)
        print("Seleccione una opción:")
        print("1. Pruebas")
        print("2. Guardar Automata")
        print("3. Cargar Automata")
        print("4. Salir")
        # Obtener la opción del usuario
        opcion_elegida = input("Ingrese el número de la opción deseada: ")

        # Manejar la opción elegida
        if opcion_elegida == "4":
            print("Saliendo del menú")
            break # Salir del bucle si la opción es '6' (Salir)
        else:
            manejar_opcion(opcion_elegida)
    
    

def manejar_opcion(opcion):
    print(f"Ha seleccionado la opción {opcion}.")
    if opcion == "1":
        AutomataFinito.definir_automata()
        # Aquí puedes agregar más lógica si es necesario después de definir el autómata
    elif opcion == "2":
        # Lógica para la opción 2
        pass
    elif opcion == "3":
        # Lógica para la opción 3
        pass
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 5.")
