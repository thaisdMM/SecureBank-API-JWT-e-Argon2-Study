from .user_register import UserRegister


class MockUserRepository:
    def __init__(self) -> None:
        # vai salvar os dados do registry_user
        self.registry_user_attributes = {}

    def registry_user(self, username: str, password: str) -> None:
        self.registry_user_attributes["username"] = username
        self.registry_user_attributes["password"] = password


def test_registry():
    repository = MockUserRepository()
    conttroller = UserRegister(repository)

    username = "olaMundo"
    password = "myPassword"

    response = conttroller.registry(username, password)
    # print()
    # print(response)
    # print(repository.registry_user_attributes) # para ver se o password é o hashed, no output está correto

    assert response["type"] == "User"
    assert response["username"] == username

    assert repository.registry_user_attributes["username"] == username
    assert repository.registry_user_attributes["password"] is not None
    assert repository.registry_user_attributes["password"] != password

