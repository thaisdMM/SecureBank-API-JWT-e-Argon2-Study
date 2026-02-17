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

    def edit_balance(self, user_id: int, new_balance: float) -> None:
        cursor = self._connection.cursor()
        cursor.execute(
            """
            UPDATE users
            SET balance = ?
            WHERE id = ?
            """,
            (new_balance, user_id),
        )
        self._connection.commit()

    def get_user_by_username(self, username: str):
        cursor = self._connection.cursor()

        cursor.execute(
            """
            SELECT id, username, password
            FROM users
            WHERE username = ?
            """,
            (username,),
            # quando usa o select tem que por uma virgula a mais - retorno é tupla
        )
        user = cursor.fetchone()
        return user
