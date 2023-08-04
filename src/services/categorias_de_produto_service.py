from typing import List
from src.interfaces.categorias_de_produto_interfaces import (
    CategoriaDeProdutoRepositoryInterface,
    CategoriaDeProdutoServiceInterface,
)
from src.models.tables.categorias_de_produto_models import (
    CategoriaDeProdutoModel,
    CategoriaDeProdutoWithoutIdModel,
)
from src.infra.db.repositories.categorias_de_produto_repositories import (
    CategoriaDeProdutoRepository,
)
from src.validation.categorias_de_produto_validation import (
    validate_categoria_de_produto,
    validate_categoria_de_produto_optional_fields,
)
from src.validation.common_validations import string_validate


class CategoriaDeProdutoService(CategoriaDeProdutoServiceInterface):
    def __init__(
        self,
        repository: CategoriaDeProdutoRepositoryInterface = CategoriaDeProdutoRepository(),
    ):
        self.__repository = repository

    def insert_categoria_de_produto(
        self, data: CategoriaDeProdutoWithoutIdModel
    ) -> None:
        validate_categoria_de_produto(
            data=data.__dict__, categoria_id_is_required=False
        )

        self.__repository.insert_categoria_de_produto(categoria=data.categoria)

    def select_categoria_de_produto_by_nome(
        self, categoria: str
    ) -> List[CategoriaDeProdutoModel]:
        string_validate(categoria, max_len=50)
        categorias = self.__repository.select_categoria_de_produto_by_nome(
            nome=categoria
        )
        return categorias

    def select_categoria_de_produto_by_id(
        self, categoria_id: int
    ) -> List[CategoriaDeProdutoModel]:
        categorias = self.__repository.select_categoria_de_produto_by_id(
            categoria_id=categoria_id
        )
        return categorias

    def select_all_categorias_de_produto(self) -> List[CategoriaDeProdutoModel]:
        categorias = self.__repository.select_all_categorias_de_produto()
        return categorias

    def update_categoria_de_produto(self, categoria_id: int, data: dict) -> None:
        validate_categoria_de_produto_optional_fields(data=data)
        self.__repository.update_categoria_de_produto(
            categoria_id=categoria_id, categoria=data["categoria"]
        )

    def delete_categoria_de_produto(self, categoria_id: int) -> None:
        self.__repository.delete_categoria_de_produto(categoria_id)
