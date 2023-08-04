from src.models.tables.categorias_de_produto_models import (
    CategoriaDeProdutoModel,
    CategoriaDeProdutoWithoutIdModel,
)
from typing import List


def generate_categorias_de_produto(size) -> List[CategoriaDeProdutoModel]:
    data = [
        CategoriaDeProdutoModel(categoria_id=1, categoria="Eletrônicos"),
        CategoriaDeProdutoModel(categoria_id=2, categoria="Roupas"),
        CategoriaDeProdutoModel(categoria_id=3, categoria="Acessórios"),
    ]
    return data[0:size]


def generate_categorias_de_produto_without_id(
    size,
) -> List[CategoriaDeProdutoWithoutIdModel]:
    data = [
        CategoriaDeProdutoWithoutIdModel(categoria="Eletrônicos"),
        CategoriaDeProdutoWithoutIdModel(categoria="Roupas"),
        CategoriaDeProdutoWithoutIdModel(categoria="Acessórios"),
    ]
    return data[0:size]
