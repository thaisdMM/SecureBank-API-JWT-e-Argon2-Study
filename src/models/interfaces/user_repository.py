from abc import ABC, abstractmethod
from sqlite3 import Connection


class UserRepositoryInterface(ABC):

    @abstractmethod
    def registry_user(self, username: str, password: str) -> None:
        pass

    @abstractmethod
    def edit_balance(self, user_id: int, new_balance: float) -> None:
        pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> tuple[int, str, str]:
        pass
