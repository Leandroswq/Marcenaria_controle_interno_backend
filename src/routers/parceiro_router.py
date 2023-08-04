from fastapi import APIRouter, Request, Query, Body, status, Path
from src.controllers.parceiro_controller import ParceiroController
from src.adapters.request_adapter import request_adapter
from src.models.tables.parceiro_models import (
    ParceiroWithoutIdModel,
    ParceiroModelResponse,
    ParceiroUpdatedModel,
)
from src.models.http.response_model import (
    Update_response_model,
    Insert_response_model,
)

router = APIRouter()

parceiro_controller = ParceiroController()

# insert ================================


@router.post(
    "/",
    summary="Adicionar um parceiro",
    status_code=status.HTTP_201_CREATED,
)
async def insert_parceiro(
    request: Request, data: ParceiroWithoutIdModel = Body(...)
) -> Insert_response_model:
    my_request = await request_adapter(request, body=data)
    response = parceiro_controller.insert_parceiro(my_request)

    return response


# get   ================================


@router.get(
    "/",
    summary="Buscar todos parceiros",
)
async def select_all_parceiros(request: Request) -> ParceiroModelResponse:
    my_request = await request_adapter(request)
    response = parceiro_controller.select_all_parceiros(my_request)
    return response


@router.get(
    "/nome/",
    summary="Buscar parceiro por nome",
)
async def select_parceiro_by_nome(
    request: Request,
    nome: str = Query(..., description="Nome do parceiro a ser pesquisado"),
) -> ParceiroModelResponse:
    my_request = await request_adapter(request)
    response = parceiro_controller.select_parceiro_by_nome(my_request)

    return response


@router.get(
    "/{parceiro_id}",
    summary="Buscar parceiro por id",
)
async def select_parceiro_by_id(
    request: Request,
    parceiro_id: int = Path(
        ..., title="Parceiro ID", description="ID do parceiro a ser buscado"
    ),
) -> ParceiroModelResponse:
    my_request = await request_adapter(request, path_params=[parceiro_id])
    response = parceiro_controller.select_parceiro_by_id(my_request)
    return response


# put  ================================


@router.put(
    "/{parceiro_id}",
    summary="Atualizar dados de um parceiro",
)
async def update_parceiro(
    request: Request,
    data: ParceiroUpdatedModel = Body(...),
    parceiro_id: int = Path(
        ..., title="Parceiro ID", description="ID do parceiro a ser atualizado"
    ),
) -> Update_response_model:
    body = await request.json()
    my_request = await request_adapter(
        request,
        body,
        path_params=[parceiro_id],
    )
    response = parceiro_controller.update_parceiro(my_request)

    return response


# delete  ================================


@router.delete(
    "/{parceiro_id}",
    summary="Deletar um parceiro",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_parceiro(
    request: Request,
    parceiro_id: int = Path(
        ..., title="Parceiro ID", description="ID do parceiro a ser deletado"
    ),
) -> None:
    my_request = await request_adapter(
        request,
        path_params=[parceiro_id],
    )
    parceiro_controller.delete_parceiro(my_request)

    return
