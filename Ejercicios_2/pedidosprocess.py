from Cliente import Cliente, ClienteVIP
from Pedido import Pedido

class ProcesadorPedidos:
    def __init__(self):
        self.pedidos = []

    def nuevo_pedido(self):
        id_cliente = input("ID Cliente: ")
        nombre = input("Nombre Cliente: ")
        contacto = input("Contacto Cliente: ")
        tipo = input("Tipo (regular/vip): ").lower()

        if tipo == "vip":
            descuento = float(input("Descuento VIP (%): "))
            cliente = ClienteVIP(id_cliente, nombre, contacto, descuento)
        else:
            cliente = Cliente(id_cliente, nombre, contacto)

        productos = []
        while True:
            nombre_prod = input("Producto (o 'fin' para terminar): ")
            if nombre_prod.lower() == "fin":
                break
            precio = float(input("Precio: "))
            productos.append((nombre_prod, precio))

        pedido = Pedido(cliente, productos)
        pedido.calcular_total()
        self.pedidos.append(pedido)

        print("\nPedido creado:\n", pedido)
