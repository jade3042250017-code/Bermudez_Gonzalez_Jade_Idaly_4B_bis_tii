import mysql.connector


class ProductModel:
    def __init__(self):
        self.config = {
            "host": "localhost",
            "user": "root",
            "password": "",
            "database": "products"
        }

    def conectar(self):
        try:
            return mysql.connector.connect(**self.config)
        except mysql.connector.Error as error:
            print("Error al conectar con MySQL:", error)
            return None

    def obtener_productos(self):
        conexion = self.conectar()
        if conexion is None:
            return []
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id, name, price FROM products")
            return cursor.fetchall()
        finally:
            cursor.close()
            conexion.close()

    def agregar_producto(self, name, price):
        conexion = self.conectar()
        if conexion is None:
            return False
        try:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (name, price))
            conexion.commit()
            return True
        except mysql.connector.Error as error:
            print("Error al insertar producto:", error)
            return False
        finally:
            cursor.close()
            conexion.close()