import mysql.connector
from mysql.connector import Error
from Controller.config import DB_config

class Database_connection:
    def __init__(self):
        self.config = DB_config

    def obtener_conexion(self):
        try:
            conexion = mysql.connector.connect(**self.config)
            if conexion.is_connected():
                return conexion
        except Error as e:
            print(f"Error al conectar con MySQL: {e}")
            return None

    def ejecutar_consulta(self, query, params=()):
        conexion = self.obtener_conexion()
        if not conexion:
            return None

        cursor = conexion.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            if query.strip().upper().startswith("SELECT"):
                resultados = cursor.fetchall()
                return resultados
            else:
                conexion.commit()
                return True
        except Error as e:
            print(f"Error en la consulta SQL: {e}")
            return None
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()