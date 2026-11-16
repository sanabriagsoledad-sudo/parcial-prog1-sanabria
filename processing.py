
"""
Módulo de procesamiento para el sistema CodeTest.

Implementa cálculos de promedios, métricas estadísticas, búsqueda lineal,
ordenamiento burbuja sobre listas paralelas y operaciones con cadenas.
"""

NOTA_REVISION = 4
NOTA_CONTRATABLE = 6



def calcular_promedios(notas_tecnica, notas_psico):
    """Calcula el promedio entre prueba técnica y psicotécnica por candidato."""
    promedios = []

    for i in range(len(notas_tecnica)):
        promedio = (notas_tecnica[i] + notas_psico[i]) / 2
        promedios = promedios + [promedio]

    return promedios



def calcular_promedio_general(promedios):
    """Calcula el promedio general de toda la camada de postulantes."""
    acumulador = 0

    for i in range(len(promedios)):
        acumulador = acumulador + promedios[i]

    return acumulador / len(promedios)



def buscar_indice_mejor_promedio(promedios):
    """Retorna el índice del postulante con el promedio más alto."""
    indice_mejor = 0

    for i in range(1, len(promedios)):
        if promedios[i] > promedios[indice_mejor]:
            indice_mejor = i

    return indice_mejor



def buscar_indice_peor_promedio(promedios):
    """Retorna el índice del postulante con el promedio más bajo."""
    indice_peor = 0

    for i in range(1, len(promedios)):
        if promedios[i] < promedios[indice_peor]:
            indice_peor = i

    return indice_peor



def contar_contratables(promedios):
    """Cuenta cuántos postulantes tienen promedio mayor o igual a 6."""
    cantidad = 0

    for i in range(len(promedios)):
        if promedios[i] >= NOTA_CONTRATABLE:
            cantidad += 1

    return cantidad



def contar_en_revision(promedios):
    """Cuenta cuántos postulantes tienen promedio >= 4 y < 6."""
    cantidad = 0

    for i in range(len(promedios)):
        if NOTA_REVISION <= promedios[i] < NOTA_CONTRATABLE:
            cantidad += 1

    return cantidad



def contar_descartados(promedios):
    """Cuenta cuántos postulantes tienen promedio menor a 4."""
    cantidad = 0

    for i in range(len(promedios)):
        if promedios[i] < NOTA_REVISION:
            cantidad += 1

    return cantidad



def ordenar_burbuja_descendente(nombres, notas_tecnica, notas_psico, promedios):
    """Ordena las listas paralelas de mayor a menor promedio con burbuja."""
    cantidad = len(promedios)

    for pasada in range(cantidad - 1):
        for i in range(cantidad - 1 - pasada):
            if promedios[i] < promedios[i + 1]:
                auxiliar = promedios[i]
                promedios[i] = promedios[i + 1]
                promedios[i + 1] = auxiliar

                auxiliar = nombres[i]
                nombres[i] = nombres[i + 1]
                nombres[i + 1] = auxiliar

                auxiliar = notas_tecnica[i]
                notas_tecnica[i] = notas_tecnica[i + 1]
                notas_tecnica[i + 1] = auxiliar

                auxiliar = notas_psico[i]
                notas_psico[i] = notas_psico[i + 1]
                notas_psico[i + 1] = auxiliar



def buscar_postulante(nombres, nombre_buscado):
    """Busca un postulante por nombre exacto y retorna su índice o -1."""
    for i in range(len(nombres)):
        if nombres[i] == nombre_buscado:
            return i

    return -1



def contar_vocales(texto):
    """Cuenta manualmente la cantidad de vocales en una cadena de texto."""
    vocales = "aeiouAEIOU"
    cantidad = 0

    for i in range(len(texto)):
        caracter = texto[i]

        for j in range(len(vocales)):
            if caracter == vocales[j]:
                cantidad += 1

    return cantidad



def invertir_texto(texto):
    """Invierte el orden de los caracteres de una cadena sin atajos."""
    invertido = ""

    for i in range(len(texto)):
        invertido = texto[i] + invertido

    return invertido