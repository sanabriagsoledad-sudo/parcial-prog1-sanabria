
"""
CodeTest: sistema de gestión de entrevistas técnicas por consola.

Módulo principal encargado de coordinar el menú interactivo, la carga
de postulantes y la visualización de reportes y estadísticas.
"""

import procesamiento
import validaciones



def mostrar_menu():
    """Despliega en consola las opciones del menú principal."""
    print()
    print("===== GESTIÓN DE ENTREVISTAS =====")
    print()
    print("1. Cargar postulantes")
    print("2. Mostrar listado general")
    print("3. Mostrar estadísticas del proceso")
    print("4. Ver ranking de postulantes (ordenado)")
    print("5. Buscar postulante")
    print("6. Analizar nombre de candidato")
    print("0. Salir")



def mostrar_listado(nombres, notas_tecnica, notas_psico, promedios):
    """Muestra en pantalla los datos y promedios de todos los postulantes."""
    print()
    for i in range(len(nombres)):
        print(f"{i + 1}. {nombres[i]} | Prueba Técnica: {notas_tecnica[i]} "
              f"| Psicotécnica: {notas_psico[i]} | Promedio: {promedios[i]}")



def mostrar_estadisticas(nombres, promedios):
    """Calcula y muestra métricas globales y conteo por estado."""
    general = procesamiento.calcular_promedio_general(promedios)
    mejor = procesamiento.buscar_indice_mejor_promedio(promedios)
    peor = procesamiento.buscar_indice_peor_promedio(promedios)
    contratables = procesamiento.contar_contratables(promedios)
    en_revision = procesamiento.contar_en_revision(promedios)
    descartados = procesamiento.contar_descartados(promedios)

    print()
    print(f"Promedio general de la camada: {general}")
    print(f"Mejor promedio: {promedios[mejor]} | Candidato: {nombres[mejor]}")
    print(f"Peor promedio: {promedios[peor]} | Candidato: {nombres[peor]}")
    print(f"Contratables (>= 6): {contratables} postulantes")
    print(f"En revisión (4 a 5.99): {en_revision} postulantes")
    print(f"Descartados (< 4): {descartados} postulantes")



def mostrar_ranking(nombres, notas_tecnica, notas_psico, promedios):
    """Ordena los postulantes de mayor a menor promedio y muestra el ranking."""
    procesamiento.ordenar_burbuja_descendente(
        nombres, notas_tecnica, notas_psico, promedios
    )
    print()
    print("---- Orden de Mérito (Ranking) ----")
    mostrar_listado(nombres, notas_tecnica, notas_psico, promedios)



def buscar_y_mostrar(nombres, notas_tecnica, notas_psico, promedios):
    """Pide un nombre y muestra las calificaciones del postulante si existe."""
    buscado = input("Ingrese el nombre del postulante a buscar: ")
    posicion = procesamiento.buscar_postulante(nombres, buscado)

    if posicion == -1:
        print("El postulante no se encuentra registrado.")
    else:
        print(f"Postulante: {nombres[posicion]} | "
              f"Técnica: {notas_tecnica[posicion]} | "
              f"Psicotécnica: {notas_psico[posicion]} | "
              f"Promedio: {promedios[posicion]}")



def analizar_nombre():
    """Solicita un nombre válido y muestra su cantidad de vocales e inverso."""
    nombre = validaciones.pedir_nombre()
    vocales = procesamiento.contar_vocales(nombre)
    invertido = procesamiento.invertir_texto(nombre)

    print(f"La cantidad de vocales es: {vocales}")
    print(f"El nombre invertido es: {invertido}")



def main():
    """Función principal que controla el ciclo de ejecución del sistema."""
    nombres = []
    notas_tecnica = []
    notas_psico = []
    promedios = []
    opcion = ""

    while opcion != "0":
        mostrar_menu()
        opcion = input("Elegí una opción: ")
        hay_datos = len(nombres) > 0

        match opcion:
            case "1":
                nombres = []
                notas_tecnica = []
                notas_psico = []
                cantidad = validaciones.pedir_cantidad()

                for i in range(cantidad):
                    print()
                    print(f"Postulante {i + 1} de {cantidad}")
                    nombres = nombres + [validaciones.pedir_nombre()]
                    print("Prueba técnica:")
                    notas_tecnica = notas_tecnica + [validaciones.pedir_nota()]
                    print("Entrevista psicotécnica:")
                    notas_psico = notas_psico + [validaciones.pedir_nota()]

                promedios = procesamiento.calcular_promedios(
                    notas_tecnica, notas_psico
                )
                print()
                print("Postulantes cargados correctamente.")

            case "2" | "3" | "4" | "5" if not hay_datos:
                print("Primero cargá los postulantes (opción 1).")

            case "2":
                mostrar_listado(nombres, notas_tecnica, notas_psico, promedios)

            case "3":
                mostrar_estadisticas(nombres, promedios)

            case "4":
                mostrar_ranking(nombres, notas_tecnica, notas_psico, promedios)

            case "5":
                buscar_y_mostrar(nombres, notas_tecnica, notas_psico, promedios)

            case "6":
                analizar_nombre()

            case "0":
                print("¡Hasta luego!")

            case _:
                print("Opción inexistente. Probá de nuevo.")


main()