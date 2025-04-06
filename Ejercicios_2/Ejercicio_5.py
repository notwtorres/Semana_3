# Crear una clase Cliente con atributos básicos (por ejemplo, ID, nombre y contacto) y una clase
# Pedido que contenga información sobre el cliente, la lista de productos solicitados y el total de
# la venta. Se podrá incluir el uso de herencia para diferenciar entre tipos de clientes (por
# ejemplo, cliente regular y cliente VIP) y aplicar descuentos especiales, demostrando el uso de la
# herencia y el polimorfismo para adaptar el comportamiento de los objetos según el tipo de
# cliente.

from pedidosprocess import ProcesadorPedidos

procesador = ProcesadorPedidos()

while True:
    opcion = input("\n1. Nuevo Pedido\n2. Salir\n> ")
    
    if opcion == "1":
        procesador.nuevo_pedido()
    elif opcion == "2":
        break
    else:
        print("Opción no válida.")
