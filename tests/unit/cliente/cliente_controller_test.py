from utilities.dict_utilities import compare_dicts
import pytest
from src.controllers.cliente_controller import ClienteController
from src.models.tables.cliente_models import (
    ClienteModel,
    ClienteWithoutIdModel,
    ClienteUpdateModel,
)
from src.interfaces.cliente_interfaces import ClienteServiceInterface
from pydantic import BaseModel
from typing import List
from src.models.http.response_model import (
    Update_response_model,
    Delete_response_model,
    Insert_response_model,
)
from src.models.http.request_model import HttpRequestModel
from tests.unit.cliente.cliente_mock import (
    generate_clientes,
    generate_clientes_without_id,
)


@pytest.fixture
def controller_service(mocker):
    mock_service = mocker.Mock(spec=ClienteServiceInterface)
    cliente_controller = ClienteController(service=mock_service)
    return cliente_controller, mock_service


def test_insert_cliente(controller_service):
    cliente_controller, mock_service = controller_service
    cliente_data = generate_clientes_without_id(1)[0]
    request = HttpRequestModel(body=cliente_data)

    mock_service.insert_cliente.return_value = None

    response = cliente_controller.insert_cliente(request)

    mock_service.insert_cliente.assert_called_once_with(data=cliente_data)

    assert isinstance(response, Insert_response_model)
    assert response.detail == "Inserido com sucesso"


def test_select_cliente_by_id(controller_service):
    cliente_controller, mock_service = controller_service
    cliente_id = 1
    request = HttpRequestModel(path_params=[cliente_id])

    mock_service.select_cliente_by_id.return_value = generate_clientes(1)

    response = cliente_controller.select_cliente_by_id(request)
    mock_service.select_cliente_by_id.assert_called_once()

    assert isinstance(response, BaseModel)
    assert hasattr(response, "detail")
    assert hasattr(response, "data")
    assert response.detail == "Operação efetuada com sucesso "
    assert isinstance(response.data, List)
    assert len(response.data) == 1
    assert compare_dicts(response.data[0].__dict__, generate_clientes(1)[0].__dict__)


def test_select_all_clientes(controller_service):
    cliente_controller, mock_service = controller_service

    mock_service.select_all_clientes.return_value = generate_clientes(2)

    request = HttpRequestModel()
    response = cliente_controller.select_all_clientes(request=request)

    mock_service.select_all_clientes.assert_called_once()

    assert isinstance(response, BaseModel)
    assert hasattr(response, "detail")
    assert hasattr(response, "data")
    assert response.detail == "Operação efetuada com sucesso "
    assert isinstance(response.data, List)
    assert len(response.data) == 2

    assert_data = generate_clientes(2)
    for i, cliente in enumerate(response.data):
        assert compare_dicts(response.data[i].__dict__, assert_data[i].__dict__)


def test_update_cliente(controller_service):
    cliente_controller, mock_service = controller_service
    cliente_id = 1
    cliente_data = generate_clientes_without_id(1)[0]

    request = HttpRequestModel(path_params=[cliente_id], body=cliente_data)

    mock_service.update_cliente.return_value = None

    response = cliente_controller.update_cliente(request=request)

    mock_service.update_cliente.assert_called_once_with(
        cliente_id=cliente_id, data=cliente_data
    )

    assert isinstance(response, Update_response_model)
    assert response.detail == "Atualizado com sucesso"


def test_delete_cliente(controller_service):
    cliente_controller, mock_service = controller_service
    cliente_id = 1
    request = HttpRequestModel(path_params=[cliente_id])

    mock_service.update_cliente.return_value = None

    response = cliente_controller.delete_cliente(request=request)

    mock_service.delete_cliente.assert_called_once_with(cliente_id=cliente_id)

    assert isinstance(response, Delete_response_model)
    assert response.detail == "Excluido com sucesso"
