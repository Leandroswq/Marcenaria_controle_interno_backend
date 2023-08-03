from src.interfaces.funcionario_interfaces import (
    FuncionarioControllerInterface,
    FuncionarioServiceInterface,
)
from src.models.http.request_model import HttpRequestModel
from src.services.funcionario_service import FuncionarioService
from src.models.tables.funcionario_models import FuncionarioModelResponse
from src.models.http.response_model import (
    Update_response_model,
    Delete_response_model,
    Insert_response_model,
)


class FuncionarioController(FuncionarioControllerInterface):
    def __init__(self, service: FuncionarioServiceInterface = FuncionarioService()):
        self.__service = service

    def insert_funcionario(self, request: HttpRequestModel) -> Insert_response_model:
        data = request.body
        self.__service.insert_funcionario(data=data)

        return Insert_response_model()

    def select_funcionario_by_nome(
        self, request: HttpRequestModel
    ) -> FuncionarioModelResponse:
        nome = request.query_params.get("nome")
        response = self.__service.select_funcionario_by_nome(nome=nome)

        return FuncionarioModelResponse(data=response)

    def select_funcionario_by_id(
        self, request: HttpRequestModel
    ) -> FuncionarioModelResponse:
        funcionario_id = request.path_params[0]
        response = self.__service.select_funcionario_by_id(funcionario_id)

        return FuncionarioModelResponse(data=response)

    def select_all_funcionarios(
        self, request: HttpRequestModel
    ) -> FuncionarioModelResponse:
        response = self.__service.select_all_funcionarios()

        return FuncionarioModelResponse(data=response)

    def update_funcionario(self, request: HttpRequestModel) -> Update_response_model:
        funcionario_id = int(request.path_params[0])
        data = request.body
        self.__service.update_funcionario(funcionario_id=funcionario_id, data=data)

        return Update_response_model()

    def delete_funcionario(self, request: HttpRequestModel) -> Delete_response_model:
        funcionario_id = int(request.path_params[0])
        self.__service.delete_funcionario(funcionario_id=funcionario_id)

        return Delete_response_model()
