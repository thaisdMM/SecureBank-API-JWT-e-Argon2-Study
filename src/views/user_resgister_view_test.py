import pytest
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .user_register_view import UserRegisterView


# por causa do UserRegisterView depende do controller
class MockController:
    def registry(self, username: str, password: str):
        return {"alguma": "coisa"}


def test_handle_user_register():
    body = {"username": "MyUsername", "password": "Security@123"}
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)

    response = user_register_view.handle(request)
    # print()
    # print(response)
    # # output object: <src.views.http_types.http_response.HttpResponse object at 0x10a0e6900>
    # print(response.body)
    # # output: {'data': {'alguma': 'coisa'}}

    assert isinstance(response, HttpResponse)
    assert response.body == {"data": {"alguma": "coisa"}}
    assert response.status_code == 201


def test_handle_user_register_with_validation_error():
    body = {"password": "Security@123"}
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)

    with pytest.raises(Exception, match="Invalid Input"):
        user_register_view.handle(request)
