import tkinter as tk
from models.product_model import ProductModel
from views.product_view import ProductView
from controllers.product_controller import ProductController


def main():
    root = tk.Tk()
    modelo = ProductModel()
    vista = ProductView(root)
    ProductController(modelo, vista)
    root.mainloop()


if __name__ == "__main__":
    main()