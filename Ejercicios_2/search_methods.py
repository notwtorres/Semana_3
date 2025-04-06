def busqueda_lineal(list, num):
    for i in range(len(list)):
        if list[i] == num:
            return f"Número encontrado en la posición {list[i]} de la lista"

    return f"El número {num} no se encuentra en la lista"  
    
def busqueda_binaria(list, num):
    if list != sorted(list):
        return "La lista debe de estar ordenada"
    l = 0
    r = len(list)
    
    while l <= r:
        m = (l + r) // 2
        if list[m] == num:
            return f"El número {num} se encuentra en la posición {m} de la lista"
        elif list[m] < num:
            l = m + 1
        else:
            r = m - 1
    
    return f"El número {num} no se encuentra en la lista"