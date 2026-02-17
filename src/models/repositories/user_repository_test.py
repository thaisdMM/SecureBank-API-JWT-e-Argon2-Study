from .user_repository import UserRepository
from src.models.settings.db_connection_handler import db_connection_handler
from unittest.mock import Mock

# transformar em testes unitarios


class MockCursor:
    def __init__(self) -> None:
        self.execute = Mock()
        self.fetchone = Mock()


class MockConnection:
    def __init__(self) -> None:
        self.cursor = Mock(return_valule=MockCursor())
        self.commit = Mock()


class TestRepository:

    def test_registry_user(self):
        # Cria uma conexão falsa (mockada)
        mock_connection = MockConnection()

        # Injeta essa conexão falsa no repositório
        repository = UserRepository(mock_connection)

        username = "Fred"
        password = "Yabadabadooo"

        # Executa o método que queremos testar - cria registro no db
        repository.registry_user(username, password)

        # Recupera o cursor que foi retornado pelo mock
        cursor = mock_connection.cursor.return_value
        # print()
        # print(cursor) # retorna um objeto <Mock name='mock()' id='4415705808'>
        # print(cursor.execute.call_args[0])
        # # output:
        # # ('\n            INSERT INTO users\n                (username, password, balance)\n
        # # VALUES\n                (?, ?, ?)\n            ', ('Fred', 'Yabadabadooo', 0))

        # cursor.execute.call_args guarda os argumentos da última chamada do execute
        # call_args[0] -> argumentos posicionais
        # call_args[0][0] -> SQL (string)
        # call_args[0][1] -> parâmetros (tupla)

        # Verifica se o SQL contém as partes esperadas
        assert "INSERT INTO users" in cursor.execute.call_args[0][0]
        assert "(username, password, balance)" in cursor.execute.call_args[0][0]
        assert "VALUES" in cursor.execute.call_args[0][0]

        # Verifica se os valores enviados estão corretos
        # O saldo inicial deve ser 0
        assert cursor.execute.call_args[0][1] == (username, password, 0)

    def test_edit_balance(self):
        # Cria uma conexão falsa (mockada)
        mock_connection = MockConnection()

        # Injeta essa conexão falsa no repositório
        repository = UserRepository(mock_connection)

        user_id = 234
        new_balance = 100.11

        # Executa o método que queremos testar - editar o balance do db
        repository.edit_balance(user_id, new_balance)

        # Recupera o cursor que foi retornado pelo mock
        cursor = mock_connection.cursor.return_value

        # Verifica se o SQL contém as partes esperadas
        assert "UPDATE users" in cursor.execute.call_args[0][0]
        assert "SET balance = ?" in cursor.execute.call_args[0][0]
        assert "WHERE id = ?" in cursor.execute.call_args[0][0]

        # Verifica se os valores enviados estão corretos
        # O saldo inicial deve ser 0
        assert cursor.execute.call_args[0][1] == (new_balance, user_id)
        mock_connection.commit.assert_called_once()

    def test_get_user_by_username(self):
        # Cria uma conexão falsa (mockada)
        mock_connection = MockConnection()

        # Injeta essa conexão falsa no repositório
        repository = UserRepository(mock_connection)

        username = "meuUsername"

        # Executa o método que queremos testar - editar o balance do db
        repository.get_user_by_username(username)

        # Recupera o cursor que foi retornado pelo mock
        cursor = mock_connection.cursor.return_value

        # Verifica se o SQL contém as partes esperadas
        assert "SELECT id, username, password" in cursor.execute.call_args[0][0]
        assert "FROM users" in cursor.execute.call_args[0][0]
        assert "WHERE username = ?" in cursor.execute.call_args[0][0]

        # Verifica se os valores enviados estão corretos
        # O saldo inicial deve ser 0
        assert cursor.execute.call_args[0][1] == (username,)

        cursor.fetchone.assert_called_once()
