from Controller.database_connection import Database_connection

class ProductsModel:
    def __init__(self):
        self.db = Database_connection()

    def obtener_productos(self):
        query = "SELECT * FROM products"
        return self.db.ejecutar_consulta(query)