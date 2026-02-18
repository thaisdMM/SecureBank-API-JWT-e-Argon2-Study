from src.controllers.interfaces.login_creator import LoginCreatorInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface


class LoginCreatorView(ViewInterface):
    def __init__(self, controller: LoginCreatorInterface) -> None:
        self._controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        # retirar os elementos do request, validar informações e retornar pelo response

        # pega os elementos
        username = http_request.body.get("username")
        password = http_request.body.get("password")

        # valida os elementos
        self._validate_inputs(username, password)

        # passou pela validação
        response = self._controller.create(username, password)

        return HttpResponse(body={"data": response}, status_code=200)

    # Usa o any, pois inicialmente pode ser qualquer coisas
    def _validate_inputs(self, username: any, password: any) -> None:
        if (
            not username
            or not password
            or not isinstance(username, str)
            or not isinstance(password, str)
        ):
            raise Exception("Invalid Input")
