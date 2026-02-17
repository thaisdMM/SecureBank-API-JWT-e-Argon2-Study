from src.models.interfaces.user_repository import UserRepositoryInterface


# não vai fazer a validação do token jwt, pois essa validação vai ser feita em outro arquivo ainda
class BalanceEditor:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self._user_repository = user_repository

    def edit(self, user_id: int, new_balance: float) -> dict:
        self._user_repository.edit_balance(user_id, new_balance)
        return {"type": "User", "count": 1, "new_balance": new_balance}

    # fazer depois um find_user por id para melhorar o codigo
