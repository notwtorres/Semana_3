# Desarrollar un programa que procese un conjunto de registros de ventas (por ejemplo, listas de
# diccionarios) para extraer información relevante. Los estudiantes deberán aplicar funciones
# internas como map, filter y reduce para transformar y filtrar los datos, calculando totales y
# promedios. Este ejercicio busca que los estudiantes identifiquen y aprovechen las
# funcionalidades nativas de Python para la manipulación eficiente de estructuras de datos

from functools import reduce
import os

def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

def esperar_tecla():
    input("Presione Enter para continuar...")

class Ventas:
    def __init__(self, precio, fecha, nombre):
        self.precio = precio
        self.fecha = fecha
        self.nombre = nombre
    
    def __str__(self):
        return f"Nombre => {self.nombre} Precio => {self.precio} Fecha => {self.fecha}"

class VentasDao:
    def __init__(self):
        self.ventas = []
    
    def agregar_ventas(self):
        precio = int(input("Ingrese el precio de la venta => "))
        fecha = input("Ingrese la fecha de la venta (dd/mm/aaaa) => ")
        nombre = input("Ingrese el nombre del producto vendido => ")
        self.ventas.append(Ventas(precio, fecha, nombre))
        esperar_tecla()
    
    def mostrar_ventas(self):
        for venta in self.ventas:
            print(venta)
        esperar_tecla()
    
    def calcular_promedio(self):
        promedio = sum(map(lambda x: x.precio, self.ventas))
        return promedio / len(self.ventas)
    
    def filtar_por_precios(self):
        user_input3 = int(input("Filtrar por precios mayores o menores (0: > / 1: <)"))
        filtro = int(input("Ingrese el precio => "))
        if user_input3 == 0:
            result = list(filter(lambda x: x.precio > filtro, self.ventas))
        elif user_input3 == 1:
            result = list(filter(lambda x: x.precio < filtro, self.ventas))
        else:
            print("Opción no válida")
            result = []
        for x in result:
            print(x)
        esperar_tecla()
    
    def filtrar_por_fecha(self):
        user_input = input("Ingrese la fecha (dd/mm/aaaa) => ")
        result = list(filter(lambda x: x.fecha == user_input, self.ventas))
        for x in result:
            print(x)
        esperar_tecla()
    
    def calcular_la_suma_total(self):
        print(f"Suma total => {reduce(lambda x, y: x + y.precio, self.ventas, 0)}")
        esperar_tecla()

def main():
    dao = VentasDao()
    while True:
        limpiar_consola()
        print("1. Agregar venta")
        print("2. Mostrar ventas")
        print("3. Filtrar ventas")
        print("4. Mostrar promedio de ventas")
        print("5. Mostrar la suma total de las ventas")
        print("6. Salir")
        
        user_input = int(input("Ingrese una opción => "))
        if user_input == 1:
            dao.agregar_ventas()
        elif user_input == 2:
            dao.mostrar_ventas()
        elif user_input == 3:
            print("1. Filtrar por precio")
            print("2. Filtrar por fecha")
            user_input2 = int(input("Ingrese una opción => "))
            if user_input2 == 1:
                dao.filtar_por_precios()
            elif user_input2 == 2:
                dao.filtrar_por_fecha()
            else: 
                print("Opción no válida")
                esperar_tecla()
        elif user_input == 4:
            print(dao.calcular_promedio())
            esperar_tecla()

        elif user_input == 5:
            dao.calcular_la_suma_total()
        elif user_input == 6:
            break
        else:
            print("Opción no válida")
            esperar_tecla()

main()
