# Diseñar una clase Producto que incluya atributos como código, nombre, precio y cantidad en
# stock. Además, los estudiantes deberán implementar una clase Inventario que administre una
# colección de objetos Producto, incorporando métodos para agregar, buscar, actualizar y
# eliminar productos. Este ejercicio permite modelar situaciones reales de gestión de ventas y
# refuerza el concepto de encapsulación y manejo de colecciones en programación orientada a
# objetos.

import os

class Prodcuto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Inventario:
    def __init__(self):
        self.productos = []
    
    def limpiar_consola(self):
        os.system("cls" if os.name == "nt" else "clear")
    
    def esperar_tecla(self):
        input("Presione una tecla para continuar...")
    
    def mostrar_productos(self):
        self.limpiar_consola()
        for producto in self.productos:
            print(f"Código: {producto.codigo}, Nombre: {producto.nombre}, Precio: {producto.precio}, Cantidad: {producto.cantidad}")
        self.esperar_tecla()
    
    def agregar_producto(self):
        self.limpiar_consola()
        codigo = input("Ingrese el código del producto => ")
        nombre = input("Ingrese el nombre del producto => ")
        precio = float(input("Ingrese el precio del producto => "))
        cantidad = int(input("Ingrese la cantidad del producto => "))
        self.productos.append(Prodcuto(codigo, nombre, precio, cantidad))
        self.esperar_tecla()
    
    def buscar_producto(self):
        self.limpiar_consola()
        num = int(input("Ingrese una opción \n 1. Buscar por código \n 2. Buscar por nombre \n 3. Buscar por precio \n => "))
        resultado = []
        if num == 1:
            codigo = input("Ingrese el código del producto => ")
            resultado = [p for p in self.productos if p.codigo == codigo]
        elif num == 2:
            nombre = input("Ingrese el nombre del producto => ")
            resultado = [p for p in self.productos if p.nombre == nombre]
        elif num == 3:
            num2 = int(input("Como desea filtrar \n 1. Precio menor \n 2. Precio mayor \n => "))
            precio = float(input("Ingrese el precio => "))
            if num2 == 1:
                resultado = [p for p in self.productos if p.precio < precio]
            elif num2 == 2:
                resultado = [p for p in self.productos if p.precio > precio]
        
        for p in resultado:
            print(f"Código: {p.codigo}, Nombre: {p.nombre}, Precio: {p.precio}, Cantidad: {p.cantidad}")
        
        self.esperar_tecla()
    
    def actualizar_producto(self):
        self.limpiar_consola()
        codigo = input("Ingrese el código del producto => ")
        user_input = int(input("Que desea actualizar? \n 1. Nombre \n 2. Precio \n 3. Cantidad \n => "))
        for producto in self.productos:
            if producto.codigo == codigo:
                if user_input == 1:
                    producto.nombre = input("Ingrese el nuevo nombre del producto => ")
                elif user_input == 2:
                    producto.precio = float(input("Ingrese el nuevo precio del producto => "))
                elif user_input == 3:
                    producto.cantidad = int(input("Ingrese la nueva cantidad del producto => "))
        self.esperar_tecla()
    
    def eliminar_productos(self):
        self.limpiar_consola()
        codigo = input("Ingrese el código del producto => ")
        self.productos = [p for p in self.productos if p.codigo != codigo]
        self.esperar_tecla()

def main():
    i = Inventario()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        user_input = int(input("Ingrese una opción: \n 1. Agregar Producto \n 2. Mostrar Productos \n 3. Buscar producto \n 4. Actualizar producto \n 5. Eliminar producto \n 6. Salir \n => "))
        if user_input == 1:
            i.agregar_producto()
        elif user_input == 2:
            i.mostrar_productos()
        elif user_input == 3:
            i.buscar_producto()
        elif user_input == 4:
            i.actualizar_producto()
        elif user_input == 5:
            i.eliminar_productos()
        else:
            break
        
if __name__ == "__main__":
    main()

    
            
    