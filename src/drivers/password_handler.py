from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


class PasswordHandler:
    """
    Responsável por gerar e verificar hashes de senha utilizando Argon2id.

    Esta classe encapsula a lógica de hash de senhas, garantindo que:
    - Senhas nunca sejam armazenadas em texto puro
    - A verificação seja feita de forma segura
    - O algoritmo possa ser atualizado futuramente (rehash)
    """

    def __init__(self):
        """
        Inicializa o manipulador de senhas com uma instância de PasswordHasher.

        A instância é criada uma única vez e reutilizada, garantindo:
        - Consistência de parâmetros
        - Melhor desempenho
        """
        self._password_hasher = PasswordHasher()

    def hash_password(self, password: str) -> str:
        """
        Gera um hash seguro para uma senha em texto puro usando Argon2id.

        Args:
            password (str): Senha em texto puro fornecida pelo usuário.

        Returns:
            str: Hash da senha, pronto para ser armazenado no banco de dados.
        """
        return self._password_hasher.hash(password)

    def verify_password(self, password: str, hashed_password: str) -> bool:
        """
        Verifica se uma senha em texto puro corresponde ao hash armazenado.

        A verificação é feita utilizando o algoritmo Argon2id.
        A senha fornecida nunca é descriptografada (o que não é possível),
        mas sim transformada novamente em hash para comparação segura.

        Args:
            password (str): Senha em texto puro fornecida pelo usuário.
            hashed_password (str): Hash da senha previamente armazenado.

        Returns:
            bool:
                - True se a senha corresponder ao hash.
                - False se a senha estiver incorreta.

        Raises:
            argon2.exceptions.InvalidHashError:
                Se o hash estiver corrompido ou em formato inválido.
            argon2.exceptions.VerificationError:
                Para falhas técnicas durante a verificação.

        Nota:
            Apenas a exceção VerifyMismatchError (senha incorreta)
            é tratada e retorna False.
            Outras exceções indicam problemas no sistema e devem ser
            tratadas pela camada superior da aplicação.
        """
        try:
            self._password_hasher.verify(hashed_password, password)
            return True
        except VerifyMismatchError:
            return False

    def check_password_needs_rehash(self, hashed_password: str) -> bool:
        """
        Verifica se o hash da senha precisa ser recriado com parâmetros atualizados.

        Este método deve ser utilizado após uma autenticação bem-sucedida.
        Caso retorne True, a senha deve ser novamente hasheada e o novo
        hash armazenado no banco de dados.

        Args:
            hashed_password (str): Hash da senha armazenado atualmente.

        Returns:
            bool:
                - True se o hash precisar ser atualizado (rehash).
                - False se o hash ainda estiver adequado.
        """
        return self._password_hasher.check_needs_rehash(hashed_password)
