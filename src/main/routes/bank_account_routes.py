from flask import Blueprint, jsonify

# vai usar o flask para criar as rotas e depois usar as rotas no servidor

bank_routes_bp = Blueprint("bank_routes", __name__)


@bank_routes_bp.route("/", methods=["GET"])
def hello():
    return jsonify({"hello": "world"}, 200)
