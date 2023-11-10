class AutomataFinito:
    def __init__(self):
        # Definimos los estados del autómata y el conjunto de caracteres de entrada
        self.estados = set()
        self.alfabeto = set()
        self.estado_inicial = None
        self.estados_aceptacion = set()

        # Inicializamos la tabla de transiciones como un diccionario vacío
        self.tabla_transiciones = {}

    def agregar_transicion(self, estado_actual, simbolo_entrada, estado_siguiente):
        # Añade una transición a la tabla de transiciones
        if estado_actual in self.estados and estado_siguiente in self.estados:
            if estado_actual not in self.tabla_transiciones:
                self.tabla_transiciones[estado_actual] = {}
            # Utiliza la cadena completa simbolo_entrada como clave para la transición
            self.tabla_transiciones[estado_actual][simbolo_entrada] = estado_siguiente
        else:
            print("Error: Estado no válido.")

    def imprimir_tabla_transiciones(self):
        print("\nTabla de Transiciones:")
        for estado_actual, transiciones in self.tabla_transiciones.items():
            for simbolo, estado_siguiente in transiciones.items():
                print(f"{estado_actual} --({simbolo})--> {estado_siguiente}")

    def calcular_tamano_simbolo(self):
        tamaño_simbolo = []  # Inicializa la lista vacía

        for i in range(1, len(self.estados) + 1):
            estado = str(i)
            tamaño_estado = 0  # Inicializa el tamaño del estado actual
            if estado in self.tabla_transiciones:
                transiciones = self.tabla_transiciones[estado]
                for simbolo_entrada, estado_siguiente in transiciones.items():
                    tamaño_estado += len(simbolo_entrada)  # Suma el tamaño de cada símbolo
            tamaño_simbolo.append(tamaño_estado)

        return tamaño_simbolo

    def validar_cadena(self, cadena, estado_actual, posicion):
        if posicion == len(cadena):
            if estado_actual in self.estados_aceptacion:
                print("La cadena es válida.")
                return True, [estado_actual]
            else:
                print(f"La cadena es inválida en el estado final {estado_actual}.")
                return False, [estado_actual]

        estados_recorridos = []

        if estado_actual in self.tabla_transiciones:
            for simbolo, estado_siguiente in self.tabla_transiciones[estado_actual].items():
                if cadena[posicion:].startswith(simbolo):
                    resultado, recorrido = self.validar_cadena(cadena, estado_siguiente, posicion + len(simbolo))
                    if resultado:
                        estados_recorridos.extend([estado_actual] + recorrido)
                        return True, estados_recorridos
                    else:
                        print(f"La cadena es inválida en el estado {estado_actual} con la subcadena '{simbolo}'.")
                        return False, estados_recorridos

        print(f"La cadena es inválida en el estado {estado_actual} con la subcadena '{cadena[posicion:]}'.")
        return False, [estado_actual]


# Crear una instancia del autómata
automata = AutomataFinito()

# Pedir al usuario que defina los estados
num_estados = int(input("Número de estados: "))
for i in range(num_estados):
    estado = input(f"Estado {i + 1}: ")
    automata.estados.add(estado)

# Pedir al usuario que defina el alfabeto
alfabeto_input = input("Alfabeto (sin separadores): ")
alfabeto = [char for char in alfabeto_input if not char.isspace()]
automata.alfabeto = set(alfabeto)

# Pedir al usuario que defina el estado inicial
automata.estado_inicial = input("Estado inicial: ")

# Pedir al usuario que defina los estados de aceptación o estado final
estados_aceptacion = input("Estados de aceptación (separados por espacios): ").split()
automata.estados_aceptacion = set(estados_aceptacion)

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
    automata.agregar_transicion(estado_actual, simbolo_entrada, estado_siguiente)

# Después de agregar todas las transiciones se imprime tabla de trancisiones
automata.imprimir_tabla_transiciones()

# Llamar a la función para calcular los tamaños de los símbolos
tamaños = automata.calcular_tamano_simbolo()

# Imprimir la lista de tamaños de símbolos
print("\nTamaños de símbolos:", tamaños)

# Validar la cadena y mostrar los estados recorridos
while True:
    cadena = input("\nIngrese una cadena o escriba 'salir' o 'exit' para finalizar: ")
    if cadena.lower() == 'salir' or cadena.lower() == 'exit':
        break

    # Validar la cadena y mostrar los recorridos
    resultado, estados_recorridos = automata.validar_cadena(cadena, automata.estado_inicial, 0)

    if resultado:
        print("Estados recorridos:", " -> ".join(estados_recorridos), "\n")

    else:
        print("Estados recorridos:", " -> ".join(estados_recorridos), "\n")