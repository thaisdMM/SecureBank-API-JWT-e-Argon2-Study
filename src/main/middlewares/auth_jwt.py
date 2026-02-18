from flask import request
from src.drivers.jwt_handler import JwtHandler
from src.errors.types.htt_unauthorized import HttpUnauthorizedError


# vai verificar as informações do jwt antes de views, do controllers e de realizar algo no banco de dados
def auth_jwt_verify():
    jwt_handle = JwtHandler()
    raw_token = request.headers.get("Authorization")
    # ver se realmente é do usuário que está acessando
    user_id = request.headers.get("uid")

    if not raw_token or not user_id:
        raise HttpUnauthorizedError("Invalid Auth informations")

    token = raw_token.split()[1]
    token_information = jwt_handle.decode_jwt_token(token)

    # a informação que esta dentro de token no codigo é user_id
    token_uid = token_information["user_id"]

    # se existir ambos e se o valor for igual
    if user_id and token_uid and (int(token_uid) == int(user_id)):
        return token_information

    # se não existir ou se o valor for diferente
    raise HttpUnauthorizedError("User Unauthorized")
