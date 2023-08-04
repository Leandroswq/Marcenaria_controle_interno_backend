from src.interfaces.categorias_de_produto_interfaces import (
    CategoriaDeProdutoControllerInterface,
    CategoriaDeProdutoServiceInterface,
)
from src.models.http.request_model import HttpRequestModel
from src.services.categorias_de_produto_service import CategoriaDeProdutoService
from src.models.tables.categorias_de_produto_models import (
    CategoriaDeProdutoModelResponse,
    CategoriaDeProdutoModel,
)
from src.models.http.response_model import (
    Update_response_model,
    Delete_response_model,
    Insert_response_model,
)


class CategoriaDeProdutoController(CategoriaDeProdutoControllerInterface):
    def __init__(
        self, service: CategoriaDeProdutoServiceInterface = CategoriaDeProdutoService()
    ):
        self.__service = service

    def insert_categoria_de_produto(
        self, request: HttpRequestModel
    ) -> Insert_response_model:
        data = request.body
        print(type(data), "=======================")
        self.__service.insert_categoria_de_produto(data=data)

        return Insert_response_model()

    def select_categoria_de_produto_by_nome(
        self, request: HttpRequestModel
    ) -> CategoriaDeProdutoModelResponse:
        nome = request.query_params.get("nome")
        response = self.__service.select_categoria_de_produto_by_nome(categoria=nome)

        return CategoriaDeProdutoModelResponse(data=response)

    def select_categoria_de_produto_by_id(
        self, request: HttpRequestModel
    ) -> CategoriaDeProdutoModelResponse:
        categoria_id = request.path_params[0]
        response = self.__service.select_categoria_de_produto_by_id(categoria_id)

        return CategoriaDeProdutoModelResponse(data=response)

    def select_all_categorias_de_produto(
        self, request: HttpRequestModel
    ) -> CategoriaDeProdutoModelResponse:
        response = self.__service.select_all_categorias_de_produto()

        return CategoriaDeProdutoModelResponse(data=response)

    def update_categoria_de_produto(
        self, request: HttpRequestModel
    ) -> Update_response_model:
        categoria_id = int(request.path_params[0])
        data = request.body
        self.__service.update_categoria_de_produto(categoria_id=categoria_id, data=data)

        return Update_response_model()

    def delete_categoria_de_produto(
        self, request: HttpRequestModel
    ) -> Delete_response_model:
        categoria_id = int(request.path_params[0])
        self.__service.delete_categoria_de_produto(categoria_id=categoria_id)
