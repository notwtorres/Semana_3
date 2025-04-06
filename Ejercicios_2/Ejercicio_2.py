# Se requiere que los estudiantes diseñen un módulo independiente que contenga
# implementaciones de algoritmos de ordenamiento simples (bubble sort). El objetivo es que, a
# partir de una función principal, se invoquen los métodos del módulo para ordenar una lista de
# números y demostrar la correcta separación de responsabilidades, fomentando la modularidad
# y la reutilización del código.

import bubble_sort 
list = []

n = int(input("Ingrese el número de elementos => "))

for i in range(n):
    numeros = int(input(f"Ingrese el elemento #{i} => "))
    list.append(numeros)

print(f"Lista ordenada => {bubble_sort.bubble_sort(list)}")