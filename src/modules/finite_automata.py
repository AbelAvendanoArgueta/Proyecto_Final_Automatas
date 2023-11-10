
# Definimos los estados del autómata y el conjunto de caracteres de entrada
estados = set()
alfabeto = set()
estado_inicial = None
estados_aceptacion = set()

# Inicializamos la tabla de transiciones como un diccionario vacío
tabla_transiciones = {}

def agregar_transicion(estado_actual, simbolo_entrada, estado_siguiente):
    # Añade una transición a la tabla de transiciones
    if estado_actual in estados and estado_siguiente in estados:
        if estado_actual not in tabla_transiciones:
            tabla_transiciones[estado_actual] = {}
        # Utiliza la cadena completa simbolo_entrada como clave para la transición
        tabla_transiciones[estado_actual][simbolo_entrada] = estado_siguiente
    else:
        print("Error: Estado no válido.")


def imprimir_tabla_transiciones():
    print("\nTabla de Transiciones:")
    for estado_actual, transiciones in tabla_transiciones.items():
        for simbolo, estado_siguiente in transiciones.items():
            print(f"{estado_actual} --({simbolo})--> {estado_siguiente}")

def calcular_tamano_simbolo():
    tamaño_simbolo = []  # Inicializa la lista vacía
    
    for i in range(1, len(estados) + 1):
        estado = str(i)
        tamaño_estado = 0  # Inicializa el tamaño del estado actual
        if estado in tabla_transiciones:
            transiciones = tabla_transiciones[estado]
            for simbolo_entrada, estado_siguiente in transiciones.items():
                tamaño_estado += len(simbolo_entrada)  # Suma el tamaño de cada símbolo
        tamaño_simbolo.append(tamaño_estado)
    
    return tamaño_simbolo

def validar_cadena( cadena):
    estado_actual = estado_inicial
    estados_recorridos = [estado_actual]

    # Crear un diccionario para almacenar las cadenas divididas según el tamaño del símbolo
    cadenas_divididas = {}

    # Inicializamos una variable para mantener un seguimiento de la posición en la cadena.
    posicion = 0

    # Iteramos a través de los estados y tamaños de símbolos para dividir la cadena
    for estado, tamaño in zip(estados, calcular_tamano_simbolo()):
        # Dividir la cadena en partes del tamaño correcto
        cadenas_divididas[estado] = cadena[posicion:posicion + tamaño]
        posicion += tamaño

    for estado, subcadena in cadenas_divididas.items():
        if estado in alfabeto:
            if estado_actual in tabla_transiciones and subcadena in tabla_transiciones[estado_actual]:
                # La subcadena es válida y hay una transición válida desde el estado actual
                # al estado siguiente con la subcadena dada.
                estado_actual = tabla_transiciones[estado_actual][subcadena]
                estados_recorridos.append(estado_actual)
            else:
                print(f"La cadena es inválida en el estado {estado_actual} con la subcadena '{subcadena}'.")
                return False, estados_recorridos
        else:
            print(f"La cadena contiene símbolos no válidos.")
            return False, estados_recorridos

    if estado_actual in estados_aceptacion:
        # Verifica si el estado final es un estado de aceptación.
        print(f"La cadena es válida.")
        return True, estados_recorridos
    else:
        print(f"La cadena es inválida en el estado final {estado_actual}.")
        return False, estados_recorridos

# Pedir al usuario que defina los estados
num_estados = int(input("Número de estados: "))
for i in range(num_estados):
    estado = input(f"Estado {i + 1}: ")
    estados.add(estado)

# Pedir al usuario que defina el alfabeto
alfabeto_input = input("Alfabeto (sin separadores): ")

# Crea una lista llamada 'alfabeto' utilizando una compresion de lista.
# Filtra los espacios en blanco del alfabeto ingresado el usuario.
alfabeto = [char for char in alfabeto_input if not char.isspace()]

# Convierte la lista "alfabeto"
alfabeto = set(alfabeto)

# Pedir al usuario que defina el estado inicial
estado_inicial = input("Estado inicial: ")

# Pedir al usuario que defina los estados de aceptación o estado final
estados_aceptacion = input("Estados de aceptación (separados por espacios): ").split()
estados_aceptacion = set(estados_aceptacion)

# Pedir al usuario que defina las transiciones
num_transiciones = int(input("Número de transiciones: "))

for i in range(num_transiciones):
    estado_actual = input(f"\nTransición {i + 1} - Estado actual: ")
    
    while True:
        # Solicita al usuario el símbolo de entrada
        simbolo_entrada = input(f"Transición {i + 1} - Símbolo de entrada: ")
        
        # Verifica si todos los caracteres de la cadena están en el alfabeto
        if all(char in alfabeto for char in simbolo_entrada):
            # Si todos los caracteres son válidos, sal del bucle
            break
        else:
            # Si algunos caracteres no son válidos, muestra un mensaje de error
            print("Símbolo de entrada no válido. Los símbolos deben estar en el alfabeto: " + alfabeto)
    
    estado_siguiente = input(f"Transición {i + 1} - Estado siguiente: ")
    
    # Agrega la transición al autómata
    agregar_transicion(estado_actual, simbolo_entrada, estado_siguiente)

# Después de agregar todas las transiciones se imprime tabla de trancisiones
imprimir_tabla_transiciones()

# Llamar a la función para calcular los tamaños de los símbolos
tamaños = calcular_tamano_simbolo()

# Imprimir la lista de tamaños de símbolos
print("\nTamaños de símbolos:", tamaños)

# Validar la cadena y mostrar los estados recorridos
while True:
    cadena = input("\nIngrese una cadena o escriba 'salir' o 'exit' para finalizar: ")
    if cadena.lower() == 'salir' or cadena.lower() == 'exit':
        break

    # Validar la cadena y mostrar los recorridos
    resultado, estados_recorridos = validar_cadena(cadena)
    if resultado:
        print("Estados recorridos:", " -> ".join(estados_recorridos),"\n")
    
    else:
        print("Estados recorridos:", " -> ".join(estados_recorridos),"\n")