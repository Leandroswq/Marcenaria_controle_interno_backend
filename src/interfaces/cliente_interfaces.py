from abc import ABC, abstractmethod
from typing import List
from src.models.http.request_model import HttpRequestModel
from src.models.http.response_model import (
    Update_response_model,
    Delete_response_model,
    Insert_response_model,
)
from src.models.tables.cliente_models import ClienteModel


class ClienteRepositoryInterface(ABC):
    @abstractmethod
    def insert_cliente(
        self,
        *,
        nome: str,
        sobre_nome: str,
        telefone: str,
        empresa: str,
        e_empresa: bool,
    ) -> None:
        pass

    @abstractmethod
    def select_cliente_by_nome(self, nome: str) -> List[ClienteModel]:
        pass

    @abstractmethod
    def select_cliente_by_id(self, cliente_id: int) -> List[ClienteModel]:
        pass

    @abstractmethod
    def select_all_clientes(self) -> List[ClienteModel]:
        pass

    @abstractmethod
    def update_cliente(self, *, data: dict) -> None:
        pass

    @abstractmethod
    def delete_cliente(self, cliente_id: int) -> None:
        pass


class ClienteServiceInterface(ABC):
    @abstractmethod
    def insert_cliente(self, data: dict) -> None:
        pass

    @abstractmethod
    def select_cliente_by_nome(self, data: dict) -> List[ClienteModel]:
        pass

    @abstractmethod
    def select_cliente_by_id(self, cliente_id: int) -> List[ClienteModel]:
        pass

    @abstractmethod
    def select_all_clientes(self) -> List[ClienteModel]:
        pass

    @abstractmethod
    def update_cliente(self, data: int, cliente_id: int) -> None:
        pass

    @abstractmethod
    def delete_cliente(self, cliente_id: int) -> None:
        pass


class ClienteControllerInterface(ABC):
    @abstractmethod
    def insert_cliente(self, request: HttpRequestModel) -> Insert_response_model:
        pass

    @abstractmethod
    def select_cliente_by_nome(self, request: HttpRequestModel) -> List[ClienteModel]:
        pass

    @abstractmethod
    def select_cliente_by_id(self, request: HttpRequestModel) -> List[ClienteModel]:
        pass

    @abstractmethod
    def select_all_clientes(self, request: HttpRequestModel) -> List[ClienteModel]:
        pass

    @abstractmethod
    def update_cliente(self, request: HttpRequestModel) -> Update_response_model:
        pass

    @abstractmethod
    def delete_cliente(self, request: HttpRequestModel) -> Delete_response_model:
        pass
