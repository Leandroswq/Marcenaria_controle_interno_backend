from src.interfaces.parceiro_interfaces import (
    ParceiroControllerInterface,
    ParceiroServiceInterface,
)
from src.models.http.request_model import HttpRequestModel
from src.services.parceiro_service import ParceiroService
from src.models.tables.parceiro_models import ParceiroModelResponse
from src.models.http.response_model import (
    Update_response_model,
    Delete_response_model,
    Insert_response_model,
)


class ParceiroController(ParceiroControllerInterface):
    def __init__(self, service: ParceiroServiceInterface = ParceiroService()):
        self.__service = service

    def insert_parceiro(self, request: HttpRequestModel) -> Insert_response_model:
        data = request.body
        self.__service.insert_parceiro(data=data)

        return Insert_response_model()

    def select_parceiro_by_nome(
        self, request: HttpRequestModel
    ) -> ParceiroModelResponse:
        nome = request.query_params.get("nome")
        response = self.__service.select_parceiro_by_nome(nome=nome)

        return ParceiroModelResponse(data=response)

    def select_parceiro_by_id(self, request: HttpRequestModel) -> ParceiroModelResponse:
        parceiro_id = request.path_params[0]
        response = self.__service.select_parceiro_by_id(parceiro_id)

        return ParceiroModelResponse(data=response)

    def select_all_parceiros(self, request: HttpRequestModel) -> ParceiroModelResponse:
        response = self.__service.select_all_parceiros()

        return ParceiroModelResponse(data=response)

    def update_parceiro(self, request: HttpRequestModel) -> Update_response_model:
        parceiro_id = int(request.path_params[0])
        data = request.body
        self.__service.update_parceiro(parceiro_id=parceiro_id, data=data)

        return Update_response_model()

    def delete_parceiro(self, request: HttpRequestModel) -> Delete_response_model:
        parceiro_id = int(request.path_params[0])
        self.__service.delete_parceiro(parceiro_id=parceiro_id)

        return Delete_response_model()
