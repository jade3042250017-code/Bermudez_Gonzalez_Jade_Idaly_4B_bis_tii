import tkinter as tk
from tkinter import ttk, messagebox, filedialog


class ProductView:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventario de Productos - Lab 9 (MVC + Polimorfismo)")
        self.root.geometry("620x480")
        self.root.configure(bg="#F4F6F7")
        self.root.resizable(False, False)

        lbl_titulo = tk.Label(
            root,
            text="GESTIÓN Y EXPORTACIÓN DE PRODUCTOS",
            font=("Arial", 15, "bold"),
            bg="#F4F6F7",
            fg="#1B4F72"
        )
        lbl_titulo.pack(pady=12)

        # --- Formulario para agregar producto ---
        frame_form = tk.Frame(root, bg="#F4F6F7")
        frame_form.pack(pady=5)

        tk.Label(frame_form, text="Producto:", bg="#F4F6F7", font=("Arial", 10)).grid(row=0, column=0, padx=5)
        self.entry_name = tk.Entry(frame_form, width=22, font=("Arial", 10))
        self.entry_name.grid(row=0, column=1, padx=5)

        tk.Label(frame_form, text="Precio ($):", bg="#F4F6F7", font=("Arial", 10)).grid(row=0, column=2, padx=5)
        self.entry_price = tk.Entry(frame_form, width=12, font=("Arial", 10))
        self.entry_price.grid(row=0, column=3, padx=5)

        self.btn_agregar = tk.Button(
            frame_form,
            text="Agregar",
            bg="#2874A6",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        )
        self.btn_agregar.grid(row=0, column=4, padx=8)

        # --- Área de Exportación  ---
        frame_export = tk.Frame(root, bg="#EBF5FB", bd=1, relief="groove", padx=10, pady=8)
        frame_export.pack(pady=10, fill="x", padx=25)

        tk.Label(
            frame_export,
            text="Formato de exportación:",
            bg="#EBF5FB",
            font=("Arial", 10, "bold"),
            fg="#154360"
        ).pack(side="left", padx=5)

        self.combo_formato = ttk.Combobox(
            frame_export,
            values=["CSV", "TXT", "JSON", "PDF"],
            state="readonly",
            width=12,
            font=("Arial", 10)
        )
        self.combo_formato.current(0)
        self.combo_formato.pack(side="left", padx=8)

        self.btn_exportar = tk.Button(
            frame_export,
            text="Exportar Reporte",
            bg="#1E8449",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        )
        self.btn_exportar.pack(side="left", padx=8)

        # --- Tabla de Productos ---
        columns = ("id", "name", "price")
        self.tree = ttk.Treeview(root, columns=columns, show="headings", height=12)
        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="Nombre del Producto")
        self.tree.heading("price", text="Precio ($)")

        self.tree.column("id", width=60, anchor="center")
        self.tree.column("name", width=360, anchor="w")
        self.tree.column("price", width=130, anchor="e")
        self.tree.pack(pady=10, padx=25)

    def actualizar_tabla(self, productos):
        for fila in self.tree.get_children():
            self.tree.delete(fila)
        for prod in productos:
            self.tree.insert("", tk.END, values=(prod[0], prod[1], f"${prod[2]:.2f}"))

    def obtener_datos_producto(self):
        return self.entry_name.get().strip(), self.entry_price.get().strip()

    def limpiar_formulario(self):
        self.entry_name.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)

    def obtener_formato_seleccionado(self):
        return self.combo_formato.get()

    def pedir_ruta_guardado(self, formato):
        ext = formato.lower()
        return filedialog.asksaveasfilename(
            defaultextension=f".{ext}",
            filetypes=[(f"Archivo {formato}", f"*.{ext}")],
            initialfile=f"reporte_productos.{ext}",
            title=f"Guardar reporte como {formato}"
        )

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje, parent=self.root)
        else:
            messagebox.showinfo(titulo, mensaje, parent=self.root)