from inventory import Inventario
from exceptions import ErrorInventario


def main():
    inventario = Inventario()
    print("Productos disponibles:", ", ".join(inventario.productos.keys()))
    codigo = input("Código del producto: ")

    # Bloque try para capturar errores de conversión (ValueError) o reglas del negocio (ErrorInventario)
    try:
        cantidad = int(input("Cantidad a retirar: "))
        stock_restante = inventario.retirar(codigo, cantidad)
    except ValueError:
        # Se ejecuta si el usuario ingresa texto o decimales en lugar de un entero
        print("Error: La cantidad debe ser un número entero.")
    except ErrorInventario as error:
        # Captura ProductoNoEncontrado, CantidadInvalida y StockInsuficiente propagadas
        print(f"No se pudo realizar la operación: {error}")
    else:
        # El bloque else se ejecuta únicamente si no ocurrió ninguna excepción en el try
        print(f"Retiro realizado con éxito. Stock restante de '{codigo}': {stock_restante}")


if __name__ == "__main__":
    main()