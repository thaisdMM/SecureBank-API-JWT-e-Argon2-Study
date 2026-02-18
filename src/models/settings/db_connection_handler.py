import sqlite3
from sqlite3 import Connection


# Coloquou os 2__ para esconder a classe e não importar ela diretamente, sim o objeto
class __DbConnectionHandler:
    def __init__(self) -> None:
        self._connection_string = "storage.db"
        self._connection = None

    def connect(self) -> None:
        # check_same_thread=False
        # → permite que uma conexão SQLite seja usada por múltiplas threads
        self._connection = sqlite3.connect(
            self._connection_string, check_same_thread=False
        )

    def get_connection(self) -> Connection:
        return self._connection


# objeto para ter uma conexão fixa no banco de dados
# vai utilizar esse objeto no restante do projeto
db_connection_handler = __DbConnectionHandler()
