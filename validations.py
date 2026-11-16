
"""
Módulo de validaciones para el sistema CodeTest.

Contiene las funciones encargadas de solicitar y validar por consola
la cantidad de postulantes, sus nombres y las calificaciones obtenidas.
"""

MIN_POSTULANTES = 1
MAX_POSTULANTES = 15
MIN_LONGITUD_NOMBRE = 5
MIN_NOTA = 0
MAX_NOTA = 10



def es_numero_entero(texto):
    """Verifica de forma manual si una cadena representa un entero positivo."""
    if len(texto) == 0:
        return False

    for i in range(len(texto)):
        if texto[i] < "0" or texto[i] > "9":
            return False

    return True



def validar_cantidad(cantidad):
    """Comprueba que la cantidad de postulantes esté entre 1 y 15."""
    return MIN_POSTULANTES <= cantidad <= MAX_POSTULANTES



def validar_nombre(nombre):
    """Valida longitud mínima (>= 5) y caracteres (solo letras y espacios)."""
    if len(nombre) < MIN_LONGITUD_NOMBRE:
        return False



    for i in range(len(nombre)):
        caracter = nombre[i]
        es_minuscula = "a" <= caracter <= "z"
        es_mayuscula = "A" <= caracter <= "Z"
        es_espacio = caracter == " "

        if not (es_minuscula or es_mayuscula or es_espacio):
            return False

    return True



def validar_nota(nota):
    """Comprueba que la calificación esté dentro del rango de 0 a 10."""
    return MIN_NOTA <= nota <= MAX_NOTA



def pedir_cantidad():
    """Solicita por teclado la cantidad de postulantes hasta que sea válida."""
    valido = False
    cantidad = None

    while not valido:
        texto = input("Ingrese la cantidad de postulantes (1 a 15): ")

        if es_numero_entero(texto) and validar_cantidad(int(texto)):
            cantidad = int(texto)
            valido = True
        else:
            print("Error: ingrese un número entero entre 1 y 15.")

    return cantidad



def pedir_nombre():
    """Solicita por teclado el nombre y apellido hasta que sea válido."""
    nombre = None
    valido = False

    while not valido:
        texto = input("Ingrese el nombre y apellido del postulante: ")

        if validar_nombre(texto):
            nombre = texto
            valido = True
        else:
            print("Error: el nombre debe tener al menos 5 caracteres y "
                  "contener solo letras o espacios.")

    return nombre



def pedir_nota():
    """Solicita por teclado una calificación entera entre 0 y 10."""
    nota = None
    valido = False

    while not valido:
        texto = input("Ingrese una nota (0 a 10): ")

        if es_numero_entero(texto) and validar_nota(int(texto)):
            nota = int(texto)
            valido = True
        else:
            print("Error: ingrese un número entero entre 0 y 10.")

    return nota

