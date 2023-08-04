from abc import ABC, abstractmethod
from typing import List
from src.models.http.request_model import HttpRequestModel
from src.models.http.response_model import (
    Update_response_model,
    Delete_response_model,
    Insert_response_model,
)
from src.models.tables.categorias_de_produto_models import (
    CategoriaDeProdutoModel,
    CategoriaDeProdutoWithoutIdModel,
)


class CategoriaDeProdutoRepositoryInterface(ABC):
    @abstractmethod
    def insert_categoria_de_produto(self, categoria: str) -> None:
        pass

    @abstractmethod
    def select_categoria_de_produto_by_nome(
        self, nome: str
    ) -> List[CategoriaDeProdutoModel]:
        pass

    @abstractmethod
    def select_categoria_de_produto_by_id(
        self, categoria_id: int
    ) -> List[CategoriaDeProdutoModel]:
        pass

    @abstractmethod
    def select_all_categorias_de_produto(self) -> List[CategoriaDeProdutoModel]:
        pass

    @abstractmethod
    def update_categoria_de_produto(self, categoria_id: int, categoria: str) -> None:
        pass

    @abstractmethod
    def delete_categoria_de_produto(self, categoria_id: int) -> None:
        pass


class CategoriaDeProdutoServiceInterface(ABC):
    @abstractmethod
    def insert_categoria_de_produto(
        self, data: CategoriaDeProdutoWithoutIdModel
    ) -> None:
        pass

    @abstractmethod
    def select_categoria_de_produto_by_nome(
        self, categoria: str
    ) -> List[CategoriaDeProdutoModel]:
        pass

    @abstractmethod
    def select_categoria_de_produto_by_id(
        self, categoria_id: int
    ) -> List[CategoriaDeProdutoModel]:
        pass

    @abstractmethod
    def select_all_categorias_de_produto(self) -> List[CategoriaDeProdutoModel]:
        pass

    @abstractmethod
    def update_categoria_de_produto(self, categoria_id: int, categoria: str) -> None:
        pass

    @abstractmethod
    def delete_categoria_de_produto(self, categoria_id: int) -> None:
        pass


class CategoriaDeProdutoControllerInterface(ABC):
    @abstractmethod
    def insert_categoria_de_produto(
        self, request: HttpRequestModel
    ) -> Insert_response_model:
        pass

    @abstractmethod
    def select_categoria_de_produto_by_nome(
        self, request: HttpRequestModel
    ) -> List[CategoriaDeProdutoModel]:
        pass

    @abstractmethod
    def select_categoria_de_produto_by_id(
        self, request: HttpRequestModel
    ) -> List[CategoriaDeProdutoModel]:
        pass

    @abstractmethod
    def select_all_categorias_de_produto(
        self, request: HttpRequestModel
    ) -> List[CategoriaDeProdutoModel]:
        pass

    @abstractmethod
    def update_categoria_de_produto(
        self, request: HttpRequestModel
    ) -> Update_response_model:
        pass

    @abstractmethod
    def delete_categoria_de_produto(
        self, request: HttpRequestModel
    ) -> Delete_response_model:
        pass
