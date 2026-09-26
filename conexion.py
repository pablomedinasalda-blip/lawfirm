import mysql.connector
from mysql.connector import Error


def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="TextilPro"
        )

        if conexion.is_connected():
            print("✅ Conexión exitosa con TextilPro")
            return conexion

    except Error as e:
        print("❌ Error al conectar con TextilPro:")
        print(e)
        return None

if __name__ == "__main__":
    conexion = conectar()

    if conexion:
        conexion.close()
        print("Conexión cerrada.")