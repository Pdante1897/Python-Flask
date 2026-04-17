from flask import Flask, jsonify, request

from Routes.Api_v1 import api_bp

app = Flask(__name__)

app.register_blueprint(api_bp, url_prefix = "/api_v1")

usuarios = [
    {"id": 1, "nombre": "Juan Perez"},
    {"id": 2, "nombre": "Bryan Paez"}
]

@app.route("/")
def home():
    return "Hola mundo, esta es mi primera api en Flask"

@app.route("/usuarios", methods=["GET"])
def get_usuarios():
    return jsonify(usuarios)

@app.route("/usuarios", methods=["POST"])
def post_usuarios():
    return "Esta es una prueba con el metodo post"

@app.route("/usuarios", methods=["DELETE"])
def delete_usuarios():
    return "Esta es una prueba con el metodo delete"

@app.route("/usuarios", methods=["PUT"])
def put_usuarios():
    return "Esta es una prueba con el metodo put"

if __name__ == "__main__":
    app.run(debug=True)
