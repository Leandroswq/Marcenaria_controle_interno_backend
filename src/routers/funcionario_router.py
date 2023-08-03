from fastapi import APIRouter, Request, Query, Body, status, Path
from src.controllers.funcionario_controller import FuncionarioController
from src.adapters.request_adapter import request_adapter
from src.models.tables.funcionario_models import (
    FuncionarioWithoutIdModel,
    FuncionarioModelResponse,
    FuncionarioUpdatedModel,
)
from src.models.http.response_model import (
    Update_response_model,
    Insert_response_model,
)

router = APIRouter()

funcionario_controller = FuncionarioController()

# insert ================================


@router.post(
    "/",
    summary="Adicionar um funcionário",
    status_code=status.HTTP_201_CREATED,
)
async def insert_funcionario(
    request: Request, data: FuncionarioWithoutIdModel = Body(...)
) -> Insert_response_model:
    my_request = await request_adapter(request, body=data)
    response = funcionario_controller.insert_funcionario(my_request)

    return response


# get   ================================


@router.get(
    "/",
    summary="Buscar todos funcionários",
)
async def select_all_funcionarios(request: Request) -> FuncionarioModelResponse:
    my_request = await request_adapter(request)
    response = funcionario_controller.select_all_funcionarios(my_request)
    return response


@router.get(
    "/nome/",
    summary="Buscar funcionário por nome",
)
async def select_funcionario_by_nome(
    request: Request,
    nome: str = Query(..., description="Nome do funcionário a ser pesquisado"),
) -> FuncionarioModelResponse:
    my_request = await request_adapter(request)
    response = funcionario_controller.select_funcionario_by_nome(my_request)

    return response


@router.get(
    "/{funcionario_id}",
    summary="Buscar funcionário por id",
)
async def select_funcionario_by_id(
    request: Request,
    funcionario_id: int = Path(
        ..., title="Funcionário ID", description="ID do funcionário a ser buscado"
    ),
) -> FuncionarioModelResponse:
    my_request = await request_adapter(request, path_params=[funcionario_id])
    response = funcionario_controller.select_funcionario_by_id(my_request)
    return response


# put  ================================


@router.put(
    "/{funcionario_id}",
    summary="Atualizar dados de um funcionário",
)
async def update_funcionario(
    request: Request,
    data: FuncionarioUpdatedModel = Body(...),
    funcionario_id: int = Path(
        ..., title="Funcionário ID", description="ID do funcionário a ser atualizado"
    ),
) -> Update_response_model:
    body = await request.json()
    my_request = await request_adapter(
        request,
        body,
        path_params=[funcionario_id],
    )
    response = funcionario_controller.update_funcionario(my_request)

    return response


# delete  ================================


@router.delete(
    "/{funcionario_id}",
    summary="Deletar um funcionário",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_funcionario(
    request: Request,
    funcionario_id: int = Path(
        ..., title="Funcionário ID", description="ID do funcionário a ser deletado"
    ),
) -> None:
    my_request = await request_adapter(
        request,
        path_params=[funcionario_id],
    )
    funcionario_controller.delete_funcionario(my_request)

    return
