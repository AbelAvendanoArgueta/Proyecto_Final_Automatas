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
            
            # Itera sobre cada carácter en simbolo_entrada y agrega la transición
            for char in simbolo_entrada:
                if char in self.alfabeto:
                    self.tabla_transiciones[estado_actual][char] = estado_siguiente
                else:
                    print(f"Error: Símbolo '{char}' en '{simbolo_entrada}' no es válido.")
        else:
            print("Error: Estado no válido.")

    def validar_cadena(self, cadena):
        estado_actual = self.estado_inicial
        estados_recorridos = [estado_actual]

        for simbolo in cadena:
            if simbolo in self.alfabeto:
                if estado_actual in self.tabla_transiciones and simbolo in self.tabla_transiciones[estado_actual]:
                    estado_actual = self.tabla_transiciones[estado_actual][simbolo]
                    estados_recorridos.append(estado_actual)
                else:
                    print(f"La cadena es inválida en el estado {estado_actual} con el símbolo '{simbolo}'.")
                    return False, estados_recorridos
            else:
                print(f"La cadena contiene símbolos no válidos.")
                return False, estados_recorridos

        if estado_actual in self.estados_aceptacion:
            print(f"La cadena es válida.")
            return True, estados_recorridos
        else:
            print(f"La cadena es inválida en el estado final {estado_actual}.")
            return False, estados_recorridos


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
num_transiciones = int(input("Número de transiciones: ")) + 1

for i in range(num_transiciones):
    estado_actual = input(f"Transición {i + 1} - Estado actual: ")
    
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

# Validar la cadena y mostrar los estados recorridos
while True:
    cadena = input("Ingrese una cadena o escriba 'salir' o 'exit' para finalizar: ")
    if cadena.lower() == 'salir' or cadena.lower() == 'exit':
        break

    # Validar la cadena y mostrar los recorridos
    resultado, estados_recorridos = automata.validar_cadena(cadena)
    if resultado:
        print("Estados recorridos:", " -> ".join(estados_recorridos))
    
    else:
        print("La cadena no es valida.")