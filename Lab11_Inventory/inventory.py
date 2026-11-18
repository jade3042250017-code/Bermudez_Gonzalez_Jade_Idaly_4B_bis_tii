from products import Producto
from exceptions import ProductoNoEncontrado


class Inventario:
    def __init__(self):
        # Diccionario con los productos base más dos productos adicionales
        self.productos = {
            "Tonayan": Producto("Tonayan", 6),
            "Fourloko": Producto("Fourloko", 7),
            "Maruchan": Producto("Maruchan", 1),
            "Sabritas": Producto("Sabritas", 10),
            "CocaCola": Producto("CocaCola", 12),
        }

    def retirar(self, codigo, cantidad):
        # Verificar si el código de producto existe; si no, lanzar ProductoNoEncontrado
        if codigo not in self.productos:
            raise ProductoNoEncontrado(f"El producto '{codigo}' no existe en el inventario.")

        # Delegar el retiro al objeto Producto; cualquier excepción se propaga hacia main()
        return self.productos[codigo].retirar(cantidad)