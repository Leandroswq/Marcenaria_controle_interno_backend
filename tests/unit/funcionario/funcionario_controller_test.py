import pytest
from src.controllers.funcionario_controller import FuncionarioController
from src.models.tables.funcionario_models import (
    FuncionarioModel,
    FuncionarioWithoutIdModel,
    FuncionarioModelResponse,
)
from src.interfaces.funcionario_interfaces import FuncionarioServiceInterface
from typing import List
from src.models.http.response_model import (
    Update_response_model,
    Delete_response_model,
    Insert_response_model,
)
from src.models.http.request_model import HttpRequestModel
from utilities.dict_utilities import compare_dicts
from tests.unit.funcionario.funcionario_mock import (
    generate_funcionarios,
    generate_funcionarios_without_id,
)


@pytest.fixture
def controller_service(mocker):
    mock_service = mocker.Mock(spec=FuncionarioServiceInterface)
    funcionario_controller = FuncionarioController(service=mock_service)
    return funcionario_controller, mock_service


def test_insert_funcionario(controller_service):
    funcionario_controller, mock_service = controller_service
    funcionario_data = generate_funcionarios_without_id(1)[0]
    request = HttpRequestModel(body=funcionario_data)

    mock_service.insert_funcionario.return_value = None

    response = funcionario_controller.insert_funcionario(request)

    mock_service.insert_funcionario.assert_called_once_with(data=funcionario_data)

    assert isinstance(response, Insert_response_model)
    assert response.detail == "Inserido com sucesso"


def test_select_funcionario_by_id(controller_service):
    funcionario_controller, mock_service = controller_service
    funcionario_id = 1
    request = HttpRequestModel(path_params=[funcionario_id])

    mock_service.select_funcionario_by_id.return_value = generate_funcionarios(1)

    response = funcionario_controller.select_funcionario_by_id(request)
    mock_service.select_funcionario_by_id.assert_called_once()

    assert isinstance(response, FuncionarioModelResponse)
    assert response.detail == "Operação efetuada com sucesso"
    assert isinstance(response.data, List)
    assert len(response.data) == 1
    assert compare_dicts(
        response.data[0].__dict__, generate_funcionarios(1)[0].__dict__
    )


def test_select_funcionario_by_nome(controller_service):
    funcionario_controller, mock_service = controller_service
    nome = "John"
    request = HttpRequestModel(query_params={"nome": nome})

    mock_service.select_funcionario_by_nome.return_value = generate_funcionarios(1)

    response = funcionario_controller.select_funcionario_by_nome(request)
    mock_service.select_funcionario_by_nome.assert_called_once_with(nome=nome)

    assert isinstance(response, FuncionarioModelResponse)
    assert response.detail == "Operação efetuada com sucesso"
    assert isinstance(response.data, List)
    assert len(response.data) == 1
    assert compare_dicts(
        response.data[0].__dict__, generate_funcionarios(1)[0].__dict__
    )


def test_select_all_funcionarios(controller_service):
    funcionario_controller, mock_service = controller_service

    mock_service.select_all_funcionarios.return_value = generate_funcionarios(2)

    request = HttpRequestModel()
    response = funcionario_controller.select_all_funcionarios(request=request)

    mock_service.select_all_funcionarios.assert_called_once()

    assert isinstance(response, FuncionarioModelResponse)
    assert response.detail == "Operação efetuada com sucesso"
    assert isinstance(response.data, List)
    assert len(response.data) == 2

    assert_data = generate_funcionarios(2)
    for i, funcionario in enumerate(response.data):
        assert compare_dicts(response.data[i].__dict__, assert_data[i].__dict__)


def test_update_funcionario(controller_service):
    funcionario_controller, mock_service = controller_service
    funcionario_id = 1
    funcionario_data = generate_funcionarios_without_id(1)[0]

    request = HttpRequestModel(path_params=[funcionario_id], body=funcionario_data)

    mock_service.update_funcionario.return_value = None

    response = funcionario_controller.update_funcionario(request=request)

    mock_service.update_funcionario.assert_called_once_with(
        funcionario_id=funcionario_id, data=funcionario_data
    )

    assert isinstance(response, Update_response_model)
    assert response.detail == "Atualizado com sucesso"


def test_delete_funcionario(controller_service):
    funcionario_controller, mock_service = controller_service
    funcionario_id = 1
    request = HttpRequestModel(path_params=[funcionario_id])

    mock_service.update_funcionario.return_value = None

    response = funcionario_controller.delete_funcionario(request=request)

    mock_service.delete_funcionario.assert_called_once_with(
        funcionario_id=funcionario_id
    )

    assert isinstance(response, Delete_response_model)
    assert response.detail == "Excluido com sucesso"
