from .password_handler import PasswordHandler


def test_hash_password():
    minha_senha = "123RocketENois"
    password_handler = PasswordHandler()

    hashed_password = password_handler.hash_password(minha_senha)
    # print(hashed_password)

    assert isinstance(hashed_password, str)
    assert len(hashed_password) > 0
    assert hashed_password.startswith("$argon2id$")


def test_verify_password():
    minha_senha = "123RocketENois"
    password_handler = PasswordHandler()

    hashed_password = password_handler.hash_password(minha_senha)
    password_verifyer = password_handler.verify_password(minha_senha, hashed_password)
    # print(password_verifyer)

    assert isinstance(password_verifyer, bool)
    assert password_verifyer is True
