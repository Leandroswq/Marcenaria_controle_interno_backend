from fastapi import APIRouter, Request, Query, Body, status, Path
from src.controllers.categorias_de_produto_controller import (
    CategoriaDeProdutoController,
)
from src.adapters.request_adapter import request_adapter
from src.models.tables.categorias_de_produto_models import (
    CategoriaDeProdutoModelResponse,
    CategoriaDeProdutoWithoutIdModel,
)
from src.models.http.response_model import (
    Update_response_model,
    Insert_response_model,
)

router = APIRouter()

categoria_de_produto_controller = CategoriaDeProdutoController()

# insert ================================


@router.post(
    "/",
    summary="Adicionar uma categoria de produto",
    status_code=status.HTTP_201_CREATED,
)
async def insert_categoria_de_produto(
    request: Request, data: CategoriaDeProdutoWithoutIdModel = Body(...)
) -> Insert_response_model:
    my_request = await request_adapter(request, body=data)
    response = categoria_de_produto_controller.insert_categoria_de_produto(my_request)

    return response


# get   ================================


@router.get(
    "/",
    summary="Buscar todas as categorias de produto",
)
async def select_all_categorias_de_produto(
    request: Request,
) -> CategoriaDeProdutoModelResponse:
    my_request = await request_adapter(request)
    response = categoria_de_produto_controller.select_all_categorias_de_produto(
        my_request
    )
    return response


@router.get(
    "/nome/",
    summary="Buscar categoria de produto por nome",
)
async def select_categoria_de_produto_by_nome(
    request: Request,
    nome: str = Query(..., description="Nome da categoria de produto a ser pesquisada"),
) -> CategoriaDeProdutoModelResponse:
    my_request = await request_adapter(request)
    response = categoria_de_produto_controller.select_categoria_de_produto_by_nome(
        my_request
    )

    return response


@router.get(
    "/{categoria_id}",
    summary="Buscar categoria de produto por id",
)
async def select_categoria_de_produto_by_id(
    request: Request,
    categoria_id: int = Path(
        ...,
        title="Categoria de Produto ID",
        description="ID da categoria de produto a ser buscada",
    ),
) -> CategoriaDeProdutoModelResponse:
    my_request = await request_adapter(request, path_params=[categoria_id])
    response = categoria_de_produto_controller.select_categoria_de_produto_by_id(
        my_request
    )
    return response


# put  ================================


@router.put(
    "/{categoria_id}",
    summary="Atualizar dados de uma categoria de produto",
)
async def update_categoria_de_produto(
    request: Request,
    data: CategoriaDeProdutoWithoutIdModel = Body(...),
    categoria_id: int = Path(
        ...,
        title="Categoria de Produto ID",
        description="ID da categoria de produto a ser atualizada",
    ),
) -> Update_response_model:
    body = await request.json()
    my_request = await request_adapter(
        request,
        body,
        path_params=[categoria_id],
    )
    response = categoria_de_produto_controller.update_categoria_de_produto(my_request)

    return response


# delete  ================================


@router.delete(
    "/{categoria_id}",
    summary="Deletar uma categoria de produto",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_categoria_de_produto(
    request: Request,
    categoria_id: int = Path(
        ...,
        title="Categoria de Produto ID",
        description="ID da categoria de produto a ser deletada",
    ),
) -> None:
    my_request = await request_adapter(
        request,
        path_params=[categoria_id],
    )
    categoria_de_produto_controller.delete_categoria_de_produto(my_request)

    return
