import pyodbc
# -*- coding: utf-8 -*-


# Datos de conexión
name_server = 'DESKTOP-I2IIMOT\\SQLEXPRESS'
database = 'AdventureWorks2008R2'
controlador_odbc = 'ODBC Driver 17 for SQL Server'

# Cadena de conexión usando Trusted_Connection
connection_string = (
    f"DRIVER={controlador_odbc};"
    f"SERVER={name_server};"
    f"DATABASE={database};"
    f"Trusted_Connection=yes;"
)

# Función para obtener la conexión
def get_connection():
    try:
        conn = pyodbc.connect(connection_string)
        print("Conexion exitosa a la base de datos.")
        return conn
    except pyodbc.Error as e:
        print("Error al conectar a la base de datos:", e)
        raise



