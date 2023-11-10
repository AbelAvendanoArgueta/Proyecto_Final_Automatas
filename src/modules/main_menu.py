from src.modules.finite_automata import AutomataFinito

ascii_art = """
 █████╗ ██╗   ██╗████████╗ ██████╗ ███╗   ███╗ █████╗ ████████╗ █████╗     ███████╗██╗███╗   ██╗██╗████████╗ ██████╗ 
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗████╗ ████║██╔══██╗╚══██╔══╝██╔══██╗    ██╔════╝██║████╗  ██║██║╚══██╔══╝██╔═══██╗
███████║██║   ██║   ██║   ██║   ██║██╔████╔██║███████║   ██║   ███████║    █████╗  ██║██╔██╗ ██║██║   ██║   ██║   ██║
██╔══██║██║   ██║   ██║   ██║   ██║██║╚██╔╝██║██╔══██║   ██║   ██╔══██║    ██╔══╝  ██║██║╚██╗██║██║   ██║   ██║   ██║
██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║    ██║     ██║██║ ╚████║██║   ██║   ╚██████╔╝
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝    ╚═════╝ 
                                                                                                                                                                                                                                                             
"""

def imprimir_menu():
    print(ascii_art)
    print("Seleccione una opción:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Opción 4")
    print("5. Opción 5")

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
    elif opcion == "4":
        # Lógica para la opción 4
        pass
    elif opcion == "5":
        # Lógica para la opción 5
        pass
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 5.")

# Obtener la opción del usuario
opcion_elegida = input("Ingrese el número de la opción deseada: ")

# Manejar la opción elegida
manejar_opcion(opcion_elegida)
