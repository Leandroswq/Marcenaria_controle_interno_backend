from src.interfaces.cliente_interfaces import (
    ClienteControllerInterface,
    ClienteServiceInterface,
)
from src.models.http.request_model import HttpRequestModel
from src.services.cliente_service import ClienteService
from src.models.tables.cliente_models import ClienteModelResponse
from src.models.http.response_model import (
    Update_response_model,
    Delete_response_model,
    Insert_response_model,
)


class ClienteController(ClienteControllerInterface):
    def __init__(self, service: ClienteServiceInterface = ClienteService()):
        self.service = service

    def insert_cliente(self, request: HttpRequestModel) -> Insert_response_model:
        data = request.body
        self.service.insert_cliente(data=data)

        return Insert_response_model()

    def select_cliente_by_nome(self, request: HttpRequestModel) -> ClienteModelResponse:
        data = request.body["data"]
        response = self.service.select_cliente_by_nome(data)

        return ClienteModelResponse(data=response)

    def select_cliente_by_id(self, request: HttpRequestModel) -> ClienteModelResponse:
        cliente_id = request.path_params[0]
        print(cliente_id, " ==============================")
        response = self.service.select_cliente_by_id(cliente_id)

        return ClienteModelResponse(data=response)

    def select_all_clientes(self, request: HttpRequestModel) -> ClienteModelResponse:
        response = self.service.select_all_clientes()

        return ClienteModelResponse(data=response)

    def update_cliente(self, request: HttpRequestModel) -> Update_response_model:
        data = request.body
        cliente_id = request.path_params[0]
        data["id"] = cliente_id
        self.service.update_cliente(data=data, cliente_id=cliente_id)

        return Update_response_model()

    def delete_cliente(self, request: HttpRequestModel) -> Delete_response_model:
        cliente_id = request.path_params[0]
        self.service.delete_cliente(cliente_id=cliente_id)

        return Delete_response_model()
