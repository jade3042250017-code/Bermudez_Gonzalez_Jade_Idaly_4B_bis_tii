from exceptions import CantidadInvalida, StockInsuficiente


class Producto:
    def __init__(self, codigo, stock):
        self.codigo = codigo
        self.stock = stock

    def retirar(self, cantidad):
        # Validar que la cantidad sea un número entero (evitando booleanos) y mayor que cero
        if not isinstance(cantidad, int) or isinstance(cantidad, bool) or cantidad <= 0:
            raise CantidadInvalida("La cantidad a retirar debe ser un número entero mayor que cero.")

        # Validar que haya suficiente inventario disponible antes de descontar
        if cantidad > self.stock:
            raise StockInsuficiente(
                f"Stock insuficiente. Disponible: {self.stock}, solicitado: {cantidad}."
            )

        # Descontar la cantidad y retornar el stock restante
        self.stock -= cantidad
        return self.stock