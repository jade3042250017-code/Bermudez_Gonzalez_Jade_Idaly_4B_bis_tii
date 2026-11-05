import os
import tkinter as tk
from tkinter import messagebox
from Models.login_model import User
from Views.home_view import DashboardVentana

class LoginVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Acceso al Sistema")
        
        # Cargar icono según requerimiento 4a
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        icon_path = os.path.join(base_dir, "app_icon.ico")
        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)

        self.root.geometry("350x380")
        self.root.resizable(False, False)

        self._crear_interfaz()

    def _crear_interfaz(self):
        lbl_titulo = tk.Label(self.root, text="Iniciar Sesión", font=("Helvetica", 16, "bold"))
        lbl_titulo.pack(pady=20)

        lbl_usuario = tk.Label(self.root, text="Usuario:", font=("Helvetica", 10))
        lbl_usuario.pack(anchor="w", padx=30, pady=(5, 2))
        self.entry_usuario = tk.Entry(self.root, font=("Helvetica", 11))
        self.entry_usuario.pack(fill="x", padx=30)

        lbl_pass = tk.Label(self.root, text="Contraseña:", font=("Helvetica", 10))
        lbl_pass.pack(anchor="w", padx=30, pady=(15, 2))
        self.entry_pass = tk.Entry(self.root, font=("Helvetica", 11), show="*")
        self.entry_pass.pack(fill="x", padx=30)

        btn_ingresar = tk.Button(
            self.root, text="Entrar", font=("Helvetica", 11, "bold"),
            bg="#2196F3", fg="white", cursor="hand2", command=self._validar_login
        )
        btn_ingresar.pack(pady=25, fill="x", padx=30)

    def _validar_login(self):
        usuario = self.entry_usuario.get().strip()
        clave = self.entry_pass.get().strip()

        if not usuario or not clave:
            messagebox.showwarning("Atención", "Por favor, complete todos los campos.")
            return

        user_model = User(usuario, clave)
        resultado = user_model.auth()

        if resultado:
            nombre = resultado[0]['nombre']
            messagebox.showinfo("Éxito", f"Bienvenido/a {nombre}")
            self.root.destroy()  # Cierra login
            
            # Abre ventana principal
            nueva_ventana = tk.Tk()
            DashboardVentana(nueva_ventana, nombre)
            nueva_ventana.mainloop()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")