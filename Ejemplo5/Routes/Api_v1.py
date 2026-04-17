from flask import Blueprint, request, jsonify
from database.conexion import get_db_connection

#Crear conexion a la base de datos y hacer un select a la tabla pelicula
conn = get_db_connection()


api_bp = Blueprint("api_v1", __name__)



@api_bp.route("/", methods=["GET"])
def index():
    resultado = validacion(10)
    return jsonify(resultado)


def validacion(usuarios):
    if usuarios == 10:
        return "Son 10 usuarios y se cumple la condicion"
    else:
        return "Son " + str(usuarios) + " usuarios y no se cumple la condicion"

#hacer un select a la tabla pelicula
@api_bp.route("/peliculas", methods=["GET"])
def get_peliculas():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pelicula")
    peliculas = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(peliculas)

#hacer un insert a la tabla pelicula
@api_bp.route("/peliculas", methods=["POST"])
def post_peliculas():
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pelicula (titulo, director) VALUES (%s, %s)", ("Pelicula de prueba", "Director de prueba"))
    conn.commit()
    cursor.close()
    conn.close()
    return "Pelicula insertada correctamente"
