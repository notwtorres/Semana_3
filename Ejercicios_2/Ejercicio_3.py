# Desarrollar un programa para organizar diferentes algoritmos de búsqueda en un paquete
# estructurado. Los estudiantes deberán crear al menos dos módulos que contengan
# implementaciones de búsqueda lineal y búsqueda binaria, configurando adecuadamente el
# archivo init.py. Posteriormente, desde un script principal, se utilizarán estas funciones para
# localizar elementos específicos en una colección de datos, resaltando la importancia de la
# organización en proyectos de mayor envergadura.

import search_methods
list = []

n = int(input("Ingrese el número de elementos => "))

for i in range(n):
    numeros = int(input(f"Ingrese el elemento #{i} => "))
    list.append(numeros)

u = int(input("Elija un método de búsqueda: \n 1. Búsqueda lineal \n 2. Búsqueda binaria \n => "))
if u == 1:
    print(search_methods.busqueda_lineal(list, int(input("Ingrese el elemento a buscar => "))))
if u == 2:
    print(search_methods.busqueda_binaria(list, int(input("Ingrese el elemento a buscar => "))))
