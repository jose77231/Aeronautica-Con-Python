codigo = [['A', 'ALFA'], ['B', 'BRAVO'], ['C', 'CHARLIE'], ['D', 'DELTA'], ['E', 'ECHO'],
          ['F', 'FOXTROT'], ['G', 'GOLF'], ['H', 'HOTEL'], ['I', 'INDIA'], ['J', 'JULIETT'],
          ['K', 'KILO'], ['L', 'LIMA'], ['M', 'MIKE'], ['N', 'NOVEMBER'], ['O', 'OSCAR'],
          ['P', 'PAPA'], ['Q', 'QUEBEC'], ['R', 'ROMEO'], ['S', 'SIERRA'], ['T', 'TANGO'],
          ['U', 'UNIFORM'], ['V', 'VICTOR'], ['W', 'WHISKEY'], ['X', 'XRAY'], ['Y', 'YANKEE'],
          ['Z', 'ZULU']]

# Función para buscar el código de lo que haya ingresado dentro de la lista "codigo"
def buscar(letra):
    for codigo_letra in codigo:
        if codigo_letra[0] == letra:
            return codigo_letra[1]

# Solicitar al usuario que ingrese la frase
frase_ingresada = input("Ingrese la frase: ").upper()

# Lista para almacenar el código de la lista que corresponda a cada letra
codigo_aeronautico = []

# Convertir cada letra de la frase ingresada a su código aeronáutico y agregarlo a la lista
for letra in frase_ingresada:
    if letra.isalpha():  # Verificar si el carácter es una letra
        codigo_aeronautico.append(buscar(letra))
    else:
        codigo_aeronautico.append(letra)  # Conservar otros caracteres que no son letras tal cual

# Unir los códigos en una sola cadena con espacios entre ellos utilizando el método "join"
codigo_extendido = " ".join(codigo_aeronautico)

# Mostrar el código extendido
print("Código extendido:")
print(codigo_extendido)
