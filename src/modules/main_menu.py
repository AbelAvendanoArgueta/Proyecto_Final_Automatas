import os
from src.modules.finite_automata import AutomataFinito
from src.modules.save_afn import afn_save_init
from src.modules.load_afn import afn_load_init

# Crear una instancia del afn
automata = AutomataFinito()

ascii_art_1 = " █████╗ ██╗   ██╗████████╗ ██████╗ ███╗   ███╗ █████╗ ████████╗ █████╗     ███████╗██╗███╗   ██╗██╗████████╗ ██████╗ "
ascii_art_2 = "██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗████╗ ████║██╔══██╗╚══██╔══╝██╔══██╗    ██╔════╝██║████╗  ██║██║╚══██╔══╝██╔═══██╗"
ascii_art_3 = "███████║██║   ██║   ██║   ██║   ██║██╔████╔██║███████║   ██║   ███████║    █████╗  ██║██╔██╗ ██║██║   ██║   ██║   ██║"
ascii_art_4 = "██╔══██║██║   ██║   ██║   ██║   ██║██║╚██╔╝██║██╔══██║   ██║   ██╔══██║    ██╔══╝  ██║██║╚██╗██║██║   ██║   ██║   ██║"
ascii_art_5 = "██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║    ██║     ██║██║ ╚████║██║   ██║   ╚██████╔╝"
ascii_art_6 = "╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝    ╚═════╝ "                                                                                                                                                                                                                                                           

def print_header(text):
    # La función get_terminal_size() devuelve un objeto 
    # os.terminal_size que contiene el tamaño actual de la terminal.
    terminal_size = os.get_terminal_size().columns
    header = text.center(terminal_size)
    print(header)

def imprimir_menu():
    while True:
        print()
        print_header("UNIVERSIDAD PANAMERICANA DE GUATEMALA")
        print()
        print_header("Facultad de Ingeniería y Ciencias Aplicadas")
        print_header("Carrera de Ingeniería en Sistemas y Tecnologías de la Información y Comunicación")
        print()
        print_header("Deneth Javier Gómez Corado 000127597")
        print_header("Abel Fernando Avendaño Argueta 000127599")
        print_header("Brayan Alexander Ríos y Ríos 000130200")
        print_header("Jerson Eduardo Gutiérrez Gamez 000126122")
        print_header("Giancarlo Josué Contreras Sandoval 000130757")
        print()
        print_header(ascii_art_1)
        print_header(ascii_art_2)
        print_header(ascii_art_3)
        print_header(ascii_art_4)
        print_header(ascii_art_5)
        print_header(ascii_art_6)
        print("\tSeleccione una opción:\n")
        print("\t\t 1. Pruebas")
        print("\t\t 2. Guardar Automata")
        print("\t\t 3. Cargar Automata")
        print("\t\t 4. Salir/Exit")
        # Obtener la opción del usuario
        opcion_elegida = input("\n\t\tIngrese el número de la opción deseada: ")

        # Manejar la opción elegida
        if opcion_elegida == "4" or opcion_elegida.lower() == 'salir' or opcion_elegida.lower() == 'exit':
            print("\nSaliendo del menú!!")
            break # Salir del bucle si la opción es '6' (Salir)
        else:
            manejar_opcion(opcion_elegida)

def manejar_opcion(opcion):
    print(f"\n\t\tHa seleccionado la opción {opcion}.")
    if opcion == "1":
        automata.ejecutar_afn()
        # Aquí puedes agregar más lógica si es necesario después de definir el autómata
    elif opcion == "2":
        afn_save_init()
        # Lógica para la opción 2
        pass
    elif opcion == "3":
        afn_load_init()
        # Lógica para la opción 3
        pass
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 5.")
