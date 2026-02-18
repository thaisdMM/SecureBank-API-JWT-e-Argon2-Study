from flask import Blueprint, jsonify, request

from src.views.http_types.http_request import HttpRequest
from src.main.composer.user_register_composer import user_register_composer
from src.main.composer.login_creater_composer import login_creator_composer
from src.main.composer.balance_editor_compose import balance_editor_composer

from src.main.middlewares.auth_jwt import auth_jwt_verify

from src.errors.error_handler import handle_errors

# vai usar o flask para criar as rotas e depois usar as rotas no servidor

bank_routes_bp = Blueprint("bank_routes", __name__)


@bank_routes_bp.route("/bank/registry", methods=["POST"])
def registry_user():
    try:
        # não precisa preencher headers, params...
        http_request = HttpRequest(body=request.json)
        # como retorna a view pode chamar diretamenta view
        http_response = user_register_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code

    except Exception as exception:
        # tem outro http_response para o tratamento de erro
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@bank_routes_bp.route("/bank/login", methods=["POST"])
def create_login():
    try:
        http_request = HttpRequest(body=request.json)
        http_response = login_creator_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code

    except Exception as exception:
        # tem outro http_response para o tratamento de erro
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


# "PATCH" (update) - fazer alteração em algum elemento do banco
@bank_routes_bp.route("/bank/balance/<user_id>", methods=["PATCH"])
def edit_balance(user_id):
    try:
        # primeiro verifica que se está tudo certo com o token
        token_information = auth_jwt_verify()

        http_request = HttpRequest(
            body=request.json,
            params={"user_id": user_id},
            token_infos=token_information,
            headers=request.headers,
        )
        http_response = balance_editor_composer().handle(http_request)
        return jsonify(http_response.body), http_response.status_code

    except Exception as exception:
        # tem outro http_response para o tratamento de erro
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
