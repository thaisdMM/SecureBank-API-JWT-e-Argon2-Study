from src.controllers.interfaces.balance_editor import BalanceEditorInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.errors.types.http_bad_request import HttpBadRequestError
from .interfaces.view_interface import ViewInterface


class BalanceEditorView(ViewInterface):
    def __init__(self, controller: BalanceEditorInterface) -> None:
        self._controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        new_balance = http_request.body.get("new_balance")
        # vai usar o get para evitar erro ao invés de params[]
        user_id = http_request.params.get("user_id")
        # para mesmo com o token valido, alterar conta de um usuario especifico e não de outro usuario
        header_user_id = http_request.headers.get("uid")

        self._validate_inputs(new_balance, user_id, header_user_id)

        response = self._controller.edit(user_id, new_balance)

        return HttpResponse(body={"data": response}, status_code=200)

    # não vai validar o user_id, pois ele vem como str, teria que validar str de int
    def _validate_inputs(
        self, new_balance: any, user_id: any, header_user_id: any
    ) -> None:
        if (
            not new_balance
            or not user_id
            or not isinstance(new_balance, float)
            or int(header_user_id) != int(user_id)
        ):
            raise HttpBadRequestError("Invalid Input")
