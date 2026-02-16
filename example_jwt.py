from flask import Flask, jsonify
import jwt
from datetime import datetime, timedelta, timezone

app = Flask(__name__)

@app.route("/", methods=["POST"])
def login():
    """Rota que cria um token e retorna o token para o usuário"""
    token = jwt.encode(
        # conteúdo que vai estar dentro do token
        payload={
            # exp: expirando(tempo válido) - agora + 1min, depois expira e tem que gerar outro
            "exp":datetime.now(timezone.utc) + timedelta(minutes=1)
        },
        # chave de acesso, onde é feita a encriptação
        key="minhaChave",
        # Esse HS256 - padrão utilizado no mercado
        algorithm="HS256"
    )
    return jsonify ({"token": token}), 200

@app.route("/secret", methods=["POST"])
def secret():
    return jsonify ({"meu": "segredo"}), 200



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

