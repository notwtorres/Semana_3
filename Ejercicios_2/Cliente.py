class Cliente:
    def __init__(self, id_cliente, nombre, contacto):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.contacto = contacto

    def __str__(self):
        return f"ID: {self.id_cliente} | {self.nombre} | Contacto: {self.contacto}"

class ClienteVIP(Cliente):
    def __init__(self, id_cliente, nombre, contacto, descuento):
        super().__init__(id_cliente, nombre, contacto)
        self.descuento = descuento  

    def aplicar_descuento(self, total):
        return total * (1 - self.descuento / 100)

    def __str__(self):
        return super().__str__() + f" | VIP Descuento: {self.descuento}%"
