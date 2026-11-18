# Excepción base para errores relacionados con el inventario
class ErrorInventario(Exception):
    pass


# Se lanza cuando el código de producto buscado no existe en el inventario
class ProductoNoEncontrado(ErrorInventario):
    pass


# Se lanza cuando la cantidad ingresada es cero, negativa o no es un entero válido
class CantidadInvalida(ErrorInventario):
    pass


# Se lanza cuando la cantidad solicitada supera el stock disponible del producto
class StockInsuficiente(ErrorInventario):
    pass