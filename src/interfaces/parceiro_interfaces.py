from abc import ABC, abstractmethod
from typing import List
from src.models.http.request_model import HttpRequestModel
from src.models.http.response_model import (
    Update_response_model,
    Delete_response_model,
    Insert_response_model,
)
from src.models.tables.parceiro_models import ParceiroModel


class ParceiroRepositoryInterface(ABC):
    @abstractmethod
    def insert_parceiro(
        self,
        *,
        nome: str,
        sobre_nome: str,
        empresa: str,
        e_empresa: bool,
        telefone: str,
    ) -> None:
        pass

    @abstractmethod
    def select_parceiro_by_nome(self, nome: str) -> List[ParceiroModel]:
        pass

    @abstractmethod
    def select_parceiro_by_id(self, parceiro_id: int) -> List[ParceiroModel]:
        pass

    @abstractmethod
    def select_all_parceiros(self) -> List[ParceiroModel]:
        pass

    @abstractmethod
    def update_parceiro(self, *, data: dict) -> None:
        pass

    @abstractmethod
    def delete_parceiro(self, parceiro_id: int) -> None:
        pass


class ParceiroServiceInterface(ABC):
    @abstractmethod
    def insert_parceiro(self, data: dict) -> None:
        pass

    @abstractmethod
    def select_parceiro_by_nome(self, nome: str) -> List[ParceiroModel]:
        pass

    @abstractmethod
    def select_parceiro_by_id(self, parceiro_id: int) -> List[ParceiroModel]:
        pass

    @abstractmethod
    def select_all_parceiros(self) -> List[ParceiroModel]:
        pass

    @abstractmethod
    def update_parceiro(self, data: int, parceiro_id: int) -> None:
        pass

    @abstractmethod
    def delete_parceiro(self, parceiro_id: int) -> None:
        pass


class ParceiroControllerInterface(ABC):
    @abstractmethod
    def insert_parceiro(self, request: HttpRequestModel) -> Insert_response_model:
        pass

    @abstractmethod
    def select_parceiro_by_nome(self, request: HttpRequestModel) -> List[ParceiroModel]:
        pass

    @abstractmethod
    def select_parceiro_by_id(self, request: HttpRequestModel) -> List[ParceiroModel]:
        pass

    @abstractmethod
    def select_all_parceiros(self, request: HttpRequestModel) -> List[ParceiroModel]:
        pass

    @abstractmethod
    def update_parceiro(self, request: HttpRequestModel) -> Update_response_model:
        pass

    @abstractmethod
    def delete_parceiro(self, request: HttpRequestModel) -> Delete_response_model:
        pass
