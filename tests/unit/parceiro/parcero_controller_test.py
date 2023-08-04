import pytest
from src.controllers.parceiro_controller import ParceiroController
from src.models.tables.parceiro_models import (
    ParceiroModel,
    ParceiroWithoutIdModel,
    ParceiroModelResponse,
)
from src.interfaces.parceiro_interfaces import ParceiroServiceInterface
from typing import List
from src.models.http.response_model import (
    Update_response_model,
    Delete_response_model,
    Insert_response_model,
)
from src.models.http.request_model import HttpRequestModel
from utilities.dict_utilities import compare_dicts


def generate_parceiros_without_id(size) -> List[ParceiroWithoutIdModel]:
    data = [
        ParceiroWithoutIdModel(
            nome="John",
            sobre_nome="Doe",
            empresa="ABC Company",
            e_empresa=True,
            telefone="12345678901",
        ),
        ParceiroWithoutIdModel(
            nome="Jane",
            sobre_nome="Smith",
            empresa="XYZ Corp",
            e_empresa=False,
            telefone="9876543210",
        ),
    ]
    return data[0:size]


def generate_parceiros(size) -> List[ParceiroModel]:
    data = [
        ParceiroModel(
            parceiro_id=1,
            nome="John",
            sobre_nome="Doe",
            empresa="ABC Company",
            e_empresa=True,
            telefone="12345678901",
        ),
        ParceiroModel(
            parceiro_id=2,
            nome="Jane",
            sobre_nome="Smith",
            empresa="XYZ Corp",
            e_empresa=False,
            telefone="9876543210",
        ),
    ]
    return data[0:size]


@pytest.fixture
def controller_service(mocker):
    mock_service = mocker.Mock(spec=ParceiroServiceInterface)
    parceiro_controller = ParceiroController(service=mock_service)
    return parceiro_controller, mock_service


def test_insert_parceiro(controller_service):
    parceiro_controller, mock_service = controller_service
    parceiro_data = generate_parceiros_without_id(1)[0]
    request = HttpRequestModel(body=parceiro_data)

    mock_service.insert_parceiro.return_value = None

    response = parceiro_controller.insert_parceiro(request)

    mock_service.insert_parceiro.assert_called_once_with(data=parceiro_data)

    assert isinstance(response, Insert_response_model)
    assert response.detail == "Inserido com sucesso"


def test_select_parceiro_by_id(controller_service):
    parceiro_controller, mock_service = controller_service
    parceiro_id = 1
    request = HttpRequestModel(path_params=[parceiro_id])

    mock_service.select_parceiro_by_id.return_value = generate_parceiros(1)

    response = parceiro_controller.select_parceiro_by_id(request)
    mock_service.select_parceiro_by_id.assert_called_once()

    assert isinstance(response, ParceiroModelResponse)
    assert response.detail == "Operação efetuada com sucesso"
    assert isinstance(response.data, List)
    assert len(response.data) == 1
    assert compare_dicts(response.data[0].__dict__, generate_parceiros(1)[0].__dict__)


def test_select_parceiro_by_nome(controller_service):
    parceiro_controller, mock_service = controller_service
    nome = "John"
    request = HttpRequestModel(query_params={"nome": nome})

    mock_service.select_parceiro_by_nome.return_value = generate_parceiros(1)

    response = parceiro_controller.select_parceiro_by_nome(request)
    mock_service.select_parceiro_by_nome.assert_called_once_with(nome=nome)

    assert isinstance(response, ParceiroModelResponse)
    assert response.detail == "Operação efetuada com sucesso"
    assert isinstance(response.data, List)
    assert len(response.data) == 1
    assert compare_dicts(response.data[0].__dict__, generate_parceiros(1)[0].__dict__)


def test_select_all_parceiros(controller_service):
    parceiro_controller, mock_service = controller_service

    mock_service.select_all_parceiros.return_value = generate_parceiros(2)

    request = HttpRequestModel()
    response = parceiro_controller.select_all_parceiros(request=request)

    mock_service.select_all_parceiros.assert_called_once()

    assert isinstance(response, ParceiroModelResponse)
    assert response.detail == "Operação efetuada com sucesso"
    assert isinstance(response.data, List)
    assert len(response.data) == 2

    assert_data = generate_parceiros(2)
    for i, parceiro in enumerate(response.data):
        assert compare_dicts(response.data[i].__dict__, assert_data[i].__dict__)


def test_update_parceiro(controller_service):
    parceiro_controller, mock_service = controller_service
    parceiro_id = 1
    parceiro_data = generate_parceiros_without_id(1)[0]

    request = HttpRequestModel(path_params=[parceiro_id], body=parceiro_data)

    mock_service.update_parceiro.return_value = None

    response = parceiro_controller.update_parceiro(request=request)
    mock_service.update_parceiro.assert_called_once_with(
        parceiro_id=parceiro_id, data=parceiro_data
    )

    assert isinstance(response, Update_response_model)
    assert response.detail == "Atualizado com sucesso"


def test_delete_parceiro(controller_service):
    parceiro_controller, mock_service = controller_service
    parceiro_id = 1
    request = HttpRequestModel(path_params=[parceiro_id])

    mock_service.delete_parceiro.return_value = None

    response = parceiro_controller.delete_parceiro(request=request)

    mock_service.delete_parceiro.assert_called_once_with(parceiro_id=parceiro_id)

    assert isinstance(response, Delete_response_model)
    assert response.detail == "Excluido com sucesso"
