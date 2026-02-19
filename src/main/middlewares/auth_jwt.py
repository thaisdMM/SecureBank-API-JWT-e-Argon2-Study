from flask import request
from src.drivers.jwt_handler import JwtHandler
from src.errors.types.http_unauthorized import HttpUnauthorizedError


def auth_jwt_verify():
    """
    Middleware de autenticação que intercepta a requisição para validar o JWT.

    Verifica se o token está presente no cabeçalho 'Authorization' e se o
    'user_id' no token corresponde ao 'uid' enviado no cabeçalho.

    Returns:
        dict: Informações decodificadas do token caso a validação seja bem-sucedida.

    Raises:
        HttpUnauthorizedError: Se o token estiver ausente, malformado ou os IDs não coincidirem.
    """
    jwt_handle = JwtHandler()

    # O cabeçalho 'Authorization' geralmente segue o formato: "Bearer <token>"
    raw_token = request.headers.get("Authorization")
    user_id = request.headers.get("uid")

    if not raw_token or not user_id:
        raise HttpUnauthorizedError("Informações de autenticação ausentes")

    try:
        # Extrai apenas o token, ignorando a palavra 'Bearer'
        token = raw_token.split()[1]
        token_information = jwt_handle.decode_jwt_token(token)
    except (IndexError, Exception):
        # Captura erros de formato de string ou falha na decodificação do JWT
        raise HttpUnauthorizedError("Token malformado ou inválido")

    token_uid = token_information.get("user_id")

    # Validação Cruzada: Garante que o usuário logado é quem ele diz ser
    if user_id and token_uid and (int(token_uid) == int(user_id)):
        return token_information

    raise HttpUnauthorizedError("Usuário não autorizado: inconsistência de ID")
