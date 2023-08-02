from fastapi import APIRouter, Request, Query, Body, status, Path
from src.controllers.cliente_controller import ClienteController
from src.adapters.request_adapter import request_adapter
from src.models.tables.cliente_models import (
    ClienteWithoutIdModel,
    ClienteModelResponse,
    ClienteUpdatedModel,
)
from src.models.http.response_model import (
    Update_response_model,
    Delete_response_model,
    Insert_response_model,
)


router = APIRouter()

cliente_controller = ClienteController()


# insert ================================


@router.post(
    "/",
    summary="Adicionar um cliente",
    status_code=status.HTTP_201_CREATED,
)
async def insert_cliente(
    request: Request, data: ClienteWithoutIdModel = Body(...)
) -> Insert_response_model:
    my_request = await request_adapter(request, body=data)
    response = cliente_controller.insert_cliente(my_request)

    return response


# get   ================================


@router.get(
    "/",
    summary="Buscar todos clientes",
)
async def select_all_clientes(request: Request) -> ClienteModelResponse:
    my_request = await request_adapter(request)
    response = cliente_controller.select_all_clientes(my_request)
    return response


@router.get(
    "/nome/",
    summary="Buscar cliente por nome",
)
async def select_cliente_by_nome(
    request: Request,
    nome: str = Query(..., description="Nome do cliente a ser pesquisado"),
) -> ClienteModelResponse:
    my_request = await request_adapter(request)
    response = cliente_controller.select_all_clientes(my_request)

    return response


@router.get(
    "/{cliente_id}",
    summary="Buscar cliente por id",
)
async def select_cliente_by_id(
    request: Request,
    cliente_id: int = Path(
        ..., title="Cliente ID", description="ID do cliente a ser deletado"
    ),
) -> ClienteModelResponse:
    my_request = await request_adapter(request, path_params=[cliente_id])
    response = cliente_controller.select_cliente_by_id(my_request)
    return response


# put  ================================


@router.put(
    "/{cliente_id}",
    summary="Atualizar dados de um cliente",
)
async def update_cliente(
    request: Request,
    data: ClienteUpdatedModel = Body(...),
    cliente_id: int = Path(
        ..., title="Cliente ID", description="ID do cliente a ser deletado"
    ),
) -> Update_response_model:
    body = await request.json()
    my_request = await request_adapter(
        request,
        body,
        path_params=[cliente_id],
    )
    response = cliente_controller.update_cliente(my_request)

    return response


# delete  ================================


from fastapi import FastAPI, HTTPException

app = FastAPI()


class ItemNotFoundError(HTTPException):
    def __init__(self, item_id: int):
        self.message = f"Item com ID {item_id} não encontrado"
        super().__init__(status_code=404, detail={"message": self.message})


@router.delete(
    "/{cliente_id}",
    summary="Deletar um cliente",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_cliente(
    request: Request,
    cliente_id: int = Path(
        ..., title="Cliente ID", description="ID do cliente a ser deletado"
    ),
) -> None:
    my_request = await request_adapter(
        request,
        path_params=[cliente_id],
    )
    response = cliente_controller.delete_cliente(my_request)

    return
