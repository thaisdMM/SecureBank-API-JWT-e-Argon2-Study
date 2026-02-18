from src.views.http_types.http_response import HttpResponse
from .types.http_bad_request import HttpBadRequestError
from .types.http_not_found import HttpNotFoundError
from .types.htt_unauthorized import HttpUnauthorizedError


def handle_errors(error: Exception) -> HttpResponse:
    """Função para tratar os erros"""
    if isinstance(
        error, (HttpBadRequestError, HttpNotFoundError, HttpUnauthorizedError)
    ):
        return HttpResponse(
            body={"errors": [{"title": error.name, "detail": error.message}]},
            status_code=error.status_code,
        )
    # se não for nenhum dos erros acima
    return HttpResponse(
        status_code=500,
        body={"errors": [{"title": "Server Error", "detail": str(error)}]},
    )
