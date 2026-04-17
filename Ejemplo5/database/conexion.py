#conectar a la base de datos en mysql
import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootpassword",
        database="python"
    )
