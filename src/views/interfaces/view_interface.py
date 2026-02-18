from abc import ABC, abstractmethod
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


class ViewInterface(ABC):
    """Obriga todas as views a seguirem o mesmo padrão de entrada e saída."""

    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        """Define uma fronteira clara: recebe dados HTTP abstratos e devolve uma resposta abstrata."""
        pass
