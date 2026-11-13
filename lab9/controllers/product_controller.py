from exporters import CSVExporter, TXTExporter, JSONExporter, PDFExporter


class ProductController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

        self.vista.btn_agregar.config(command=self.registrar_producto)
        self.vista.btn_exportar.config(command=self.generar_reporte)

        self.cargar_productos()

    def cargar_productos(self):
        productos = self.modelo.obtener_productos()
        self.vista.actualizar_tabla(productos)

    def registrar_producto(self):
        nombre, precio_str = self.vista.obtener_datos_producto()
        if not nombre or not precio_str:
            self.vista.mostrar_mensaje("Campos vacíos", "Ingresa el nombre y el precio del producto.", "error")
            return

        try:
            precio = float(precio_str)
            if precio <= 0:
                raise ValueError
        except ValueError:
            self.vista.mostrar_mensaje("Precio inválido", "Ingresa un precio numérico mayor a cero.", "error")
            return

        if self.modelo.agregar_producto(nombre, precio):
            self.vista.limpiar_formulario()
            self.cargar_productos()
            self.vista.mostrar_mensaje("Éxito", "Producto registrado correctamente.")
        else:
            self.vista.mostrar_mensaje("Error", "No se pudo guardar en MySQL.", "error")

    def generar_reporte(self):
        productos = self.modelo.obtener_productos()
        if not productos:
            self.vista.mostrar_mensaje("Sin datos", "No hay productos en la base de datos para exportar.", "error")
            return

        formato = self.vista.obtener_formato_seleccionado()
        ruta_archivo = self.vista.pedir_ruta_guardado(formato)

        if not ruta_archivo:
            return

        exportadores = {
            "CSV": CSVExporter(),
            "TXT": TXTExporter(),
            "JSON": JSONExporter(),
            "PDF": PDFExporter(),
        }

        exportador = exportadores.get(formato)

        try:
            exportador.export(productos, ruta_archivo)
            self.vista.mostrar_mensaje("Reporte generado", f"Archivo {formato} guardado exitosamente.")
        except Exception as error:
            self.vista.mostrar_mensaje("Error al exportar", f"Ocurrió un error: {error}", "error")