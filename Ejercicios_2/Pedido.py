from Cliente import Cliente, ClienteVIP

class Pedido:
    def __init__(self, cliente, productos):
        self.cliente = cliente
        self.productos = productos  
        self.total = sum(p[1] for p in productos)

    def calcular_total(self):
        if isinstance(self.cliente, ClienteVIP):
            self.total = self.cliente.aplicar_descuento(self.total)
        return self.total

    def __str__(self):
        lista_productos = "\n".join([f"- {p[0]}: ${p[1]:.2f}" for p in self.productos])
        return f"Cliente: {self.cliente.nombre}\nProductos:\n{lista_productos}\nTotal: ${self.total:.2f}"
