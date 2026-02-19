import os
import sqlite3
from src.main.server.server import app


def init_db():
    """Inicializa o banco de dados caso ele não exista."""
    db_path = "storage.db"
    schema_path = "init/schema.sql"

    if not os.path.exists(db_path) and os.path.exists(schema_path):
        print("Iniciando banco de dados pela primeira vez...")
        with sqlite3.connect(db_path) as conn:
            with open(schema_path, "r") as f:
                conn.executescript(f.read())
        print("Banco de dados criado com sucesso!")


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=3000, debug=True)
