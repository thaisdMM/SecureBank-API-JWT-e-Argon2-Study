class HttpRequest:
    """
    Objeto de transporte de dados da requisição HTTP da aplicação.

    Esta classe abstrai os dados relevantes de uma requisição HTTP,
    desacoplando as camadas internas da aplicação do framework web.
    Seu uso permite controlar como informações da requisição entram
    no sistema, padronizando a comunicação entre controllers e serviços.
    """

    def __init__(
        self,
        body: dict = None,
        headers: dict = None,
        params: dict = None,
        token_infos: dict = None,
    ) -> None:
        self.body = body
        self.headers = headers
        self.params = params
        self.token_infos = token_infos
