import tkinter as tk
from tkinter import ttk
from Models.products_model import ProductsModel

class DashboardVentana:
    def __init__(self, root, nombre_usuario):
        self.root = root
        self.root.title("Panel Principal - Productos")
        self.root.geometry("600x400")

        lbl_bienvenida = tk.Label(
            self.root, 
            text=f"¡Bienvenido/a, {nombre_usuario}!", 
            font=("Helvetica", 14, "bold")
        )
        lbl_bienvenida.pack(pady=10)

        lbl_instruccion = tk.Label(self.root, text="Catálogo de Productos:", font=("Helvetica", 11))
        lbl_instruccion.pack(anchor="w", padx=20, pady=5)

        # Tabla para listar productos
        self.tabla = ttk.Treeview(self.root, columns=("ID", "Nombre", "Precio", "Stock"), show="headings")
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Precio", text="Precio")
        self.tabla.heading("Stock", text="Stock")

        self.tabla.column("ID", width=50, anchor="center")
        self.tabla.column("Nombre", width=200)
        self.tabla.column("Precio", width=100, anchor="e")
        self.tabla.column("Stock", width=80, anchor="center")

        self.tabla.pack(fill="both", expand=True, padx=20, pady=10)

        self._cargar_productos()

    def _cargar_productos(self):
        model = ProductsModel()
        productos = model.obtener_productos()

        if productos:
            for p in productos:
                self.tabla.insert("", "end", values=(p['id'], p['nombre'], f"${p['precio']}", p['stock']))