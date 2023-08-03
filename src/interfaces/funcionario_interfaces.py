from abc import ABC, abstractmethod
from typing import List
from src.models.http.request_model import HttpRequestModel
from src.models.http.response_model import (
    Update_response_model,
    Delete_response_model,
    Insert_response_model,
)
from src.models.tables.funcionario_models import FuncionarioModel


class FuncionarioRepositoryInterface(ABC):
    @abstractmethod
    def insert_funcionario(
        self,
        *,
        nome: str,
        sobre_nome: str,
        funcao: str,
        telefone: str,
    ) -> None:
        pass

    @abstractmethod
    def select_funcionario_by_nome(self, nome: str) -> List[FuncionarioModel]:
        pass

    @abstractmethod
    def select_funcionario_by_id(self, funcionario_id: int) -> List[FuncionarioModel]:
        pass

    @abstractmethod
    def select_all_funcionarios(self) -> List[FuncionarioModel]:
        pass

    @abstractmethod
    def update_funcionario(self, *, data: dict) -> None:
        pass

    @abstractmethod
    def delete_funcionario(self, funcionario_id: int) -> None:
        pass


class FuncionarioServiceInterface(ABC):
    @abstractmethod
    def insert_funcionario(self, data: dict) -> None:
        pass

    @abstractmethod
    def select_funcionario_by_nome(self, nome: str) -> List[FuncionarioModel]:
        pass

    @abstractmethod
    def select_funcionario_by_id(self, funcionario_id: int) -> List[FuncionarioModel]:
        pass

    @abstractmethod
    def select_all_funcionarios(self) -> List[FuncionarioModel]:
        pass

    @abstractmethod
    def update_funcionario(self, data: int, funcionario_id: int) -> None:
        pass

    @abstractmethod
    def delete_funcionario(self, funcionario_id: int) -> None:
        pass


class FuncionarioControllerInterface(ABC):
    @abstractmethod
    def insert_funcionario(self, request: HttpRequestModel) -> Insert_response_model:
        pass

    @abstractmethod
    def select_funcionario_by_nome(
        self, request: HttpRequestModel
    ) -> List[FuncionarioModel]:
        pass

    @abstractmethod
    def select_funcionario_by_id(
        self, request: HttpRequestModel
    ) -> List[FuncionarioModel]:
        pass

    @abstractmethod
    def select_all_funcionarios(
        self, request: HttpRequestModel
    ) -> List[FuncionarioModel]:
        pass

    @abstractmethod
    def update_funcionario(self, request: HttpRequestModel) -> Update_response_model:
        pass

    @abstractmethod
    def delete_funcionario(self, request: HttpRequestModel) -> Delete_response_model:
        pass
