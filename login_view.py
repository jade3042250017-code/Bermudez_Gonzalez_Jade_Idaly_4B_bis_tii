import tkinter as tk

class login_screen:
    def __init__(self, root):
        self.root = root
        self.root.tittle("System Lab 7")
        self.root.geometry("300x300")
        self.root.resizable(False, False)

        def create_interface(self):
            lbl_titulo = tk.Label(self.root, text = "Inicio de sesion", font = ("Helvetica", 20))
            lbl_titulo = tk.Label(self.root, text = "Username", font = ("Helvetica", 10))