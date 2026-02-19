import jwt
from datetime import datetime, timedelta, timezone
from typing import Dict, Any
from src.configs.jwt_configs import jwt_infos


class JwtHandler:
    """
    Classe responsável pela manipulação de JSON Web Tokens (JWT).
    Encapsula a lógica de criação e decodificação utilizando a biblioteca PyJWT.
    """

    def create_jwt_token(self, body: Dict[str, Any] = {}) -> str:
        """
        Gera um novo token JWT assinado.

        Args:
            body (dict): Dados adicionais (claims) a serem incluídos no payload.

        Returns:
            str: O token JWT codificado em formato string.
        """
        # Define o tempo de expiração baseado em UTC (padrão recomendado para sistemas distribuídos)
        expiration_time = datetime.now(timezone.utc) + timedelta(
            hours=int(jwt_infos["JWT_HOURS"])
        )

        payload = {
            "exp": expiration_time,
            **body,  # Desempacota as informações adicionais (ex: user_id) no payload
        }

        # O segredo (key) e o algoritmo garantem a integridade do token
        token = jwt.encode(
            payload=payload, key=jwt_infos["KEY"], algorithm=jwt_infos["ALGORITHM"]
        )
        return token

    def decode_jwt_token(self, token: str) -> Dict[str, Any]:
        """
        Decodifica um token JWT e verifica sua validade e assinatura.

        Args:
            token (str): O token JWT a ser validado.

        Returns:
            dict: Os dados contidos no payload do token.

        Raises:
            jwt.ExpiredSignatureError: Se o token já tiver expirado.
            jwt.InvalidTokenError: Se a assinatura for inválida ou o token estiver corrompido.
        """
        # Nota de Segurança: 'algorithms' deve ser passado como uma lista [ALGORITHM]
        token_information = jwt.decode(
            token, key=jwt_infos["KEY"], algorithms=[jwt_infos["ALGORITHM"]]
        )
        return token_information
