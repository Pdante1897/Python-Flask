from flask import Blueprint, request, jsonify

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