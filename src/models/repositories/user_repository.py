from sqlite3 import Connection


class UserRepository:
    # vai passar a conexão com o banco de dados
    # injeção de dependencia
    def __init__(self, connection: Connection) -> None:
        self._connection = connection

    # não vai encriptar aqui, é só ação no banco de dados
    def registry_user(self, username: str, password: str) -> None:
        cursor = self._connection.cursor()
        # vai usar sql direto
        cursor.execute(
            """
            INSERT INTO users
                (username, password, balance)
            VALUES
                (?, ?, ?)
            """,
            (username, password, 0),
        )
        self._connection.commit()
