# Crear una clase Factura que simule el proceso de facturación de una venta. Los estudiantes
# deberán encapsular los datos internos de la factura (como los detalles de los productos,
# cantidades, precios y descuentos) y proveer métodos para calcular el total de la venta, generar
# reportes simples y validar la integridad de la información. Este ejercicio enfatiza la importancia
# de ocultar la implementación interna y de diseñar interfaces claras y seguras para la gestión de
# transacciones comerciales.

class Factura:
    def __init__(self):
        self._productos = []  
        self._descuento = 0.0 

    def agregar_producto(self, nombre, cantidad, precio):
        """Agrega un producto a la factura."""
        if cantidad <= 0 or precio < 0:
            raise ValueError("La cantidad debe ser mayor que 0 y el precio no puede ser negativo.")
        self._productos.append({
            'nombre': nombre,
            'cantidad': cantidad,
            'precio': precio
        })

    def establecer_descuento(self, descuento):
        """Establece un descuento total para la factura."""
        if descuento < 0:
            raise ValueError("El descuento no puede ser negativo.")
        self._descuento = descuento

    def calcular_total(self):
        """Calcula el total de la factura aplicando el descuento."""
        total = sum(item['cantidad'] * item['precio'] for item in self._productos)
        total_con_descuento = total - self._descuento
        return total_con_descuento if total_con_descuento > 0 else 0.0

    def generar_reporte(self):
        """Genera un reporte simple de la factura."""
        reporte = "Reporte de Factura:\n"
        for item in self._productos:
            reporte += f"Producto: {item['nombre']}, Cantidad: {item['cantidad']}, Precio: {item['precio']:.2f}\n"
        reporte += f"Descuento: {self._descuento:.2f}\n"
        reporte += f"Total a Pagar: {self.calcular_total():.2f}\n"
        return reporte

    def validar_integridad(self):
        """Valida la integridad de la información de la factura."""
        if not self._productos:
            raise ValueError("No hay productos en la factura.")
        for item in self._productos:
            if item['cantidad'] <= 0 or item['precio'] < 0:
                raise ValueError(f"Producto {item['nombre']} tiene cantidad o precio inválido.")


if __name__ == "__main__":
    factura = Factura()
    factura.agregar_producto("Producto A", 2, 50.0)
    factura.agregar_producto("Producto B", 1, 30.0)
    factura.establecer_descuento(10.0)

    try:
        factura.validar_integridad()
        print(factura.generar_reporte())
    except ValueError as e:
        print(f"Error: {e}")