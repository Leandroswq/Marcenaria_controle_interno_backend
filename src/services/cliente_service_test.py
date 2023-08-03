import pytest

from src.errors.http_erros import ValidationException
from src.services.cliente_service import ClienteService
from src.models.tables.cliente_models import ClienteWithoutIdModel, ClienteModel
from utilities.dict_utilities import compare_dicts
from typing import List


def generate_clientes(size) -> List[ClienteModel]:
    data = [
        ClienteModel(
            client_id=1,
            nome="John",
            sobre_nome="Doe",
            telefone="12345678901",
            empresa="Example Corp",
            e_empresa=True,
        ),
        ClienteModel(
            client_id=2,
            nome="Jane",
            sobre_nome="Smith",
            telefone="9876543210",
            empresa="Test Inc",
            e_empresa=False,
        ),
    ]
    return data[0:size]


def generate_clientes_without_id(size) -> List[ClienteWithoutIdModel]:
    data = [
        ClienteWithoutIdModel(
            nome="John",
            sobre_nome="Doe",
            telefone="12345678901",
            empresa="Example Corp",
            e_empresa=True,
        ),
        ClienteWithoutIdModel(
            nome="Jane",
            sobre_nome="Smith",
            telefone="9876543210",
            empresa="Test Inc",
            e_empresa=False,
        ),
    ]
    return data[0:size]


@pytest.fixture
def service(mocker):
    mock_repository = mocker.Mock()
    cliente_service = ClienteService(repository=mock_repository)

    return cliente_service, mock_repository


def test_insert_cliente(service):
    cliente_service, mock_repository = service
    cliente_data = generate_clientes_without_id(1)[0]

    assert cliente_service.insert_cliente(data=cliente_data) is None

    cliente_data = generate_clientes_without_id(1)[0]
    mock_repository.insert_cliente.assert_called_once_with(
        nome=cliente_data.nome,
        sobre_nome=cliente_data.sobre_nome,
        telefone=cliente_data.telefone,
        empresa=cliente_data.empresa,
        e_empresa=cliente_data.e_empresa,
    )


def test_insert_cliente_invalid_data(service):
    cliente_service, mock_repository = service
    cliente_data = generate_clientes_without_id(1)[0]
    cliente_data.telefone = ""
    with pytest.raises(ValidationException):
        cliente_service.insert_cliente(data=cliente_data)


def test_select_cliente_by_id(service):
    cliente_service, mock_repository = service
    cliente_id = 1

    mock_response = generate_clientes(1)

    mock_repository.select_cliente_by_id.return_value = mock_response

    clientes = cliente_service.select_cliente_by_id(cliente_id=cliente_id)

    mock_repository.select_cliente_by_id.assert_called_once_with(cliente_id=cliente_id)

    assert isinstance(clientes, list)
    assert all(isinstance(cliente, ClienteModel) for cliente in clientes)
    assert compare_dicts(clientes[0].__dict__, generate_clientes(1)[0].__dict__)


def test_select_cliente_by_nome(service):
    cliente_service, mock_repository = service
    mock_repository.select_cliente_by_nome.return_value = generate_clientes(2)

    nome = "John"
    clientes = cliente_service.select_cliente_by_nome(nome=nome)

    mock_repository.select_cliente_by_nome.assert_called_once_with(nome=nome)

    assert isinstance(clientes, list)
    assert all(isinstance(cliente, ClienteModel) for cliente in clientes)
    assert len(clientes) == 2

    clientes_response = generate_clientes(2)

    for i, cliente in enumerate(clientes):
        assert compare_dicts(cliente.__dict__, clientes_response[i].__dict__)


def test_select_cliente_by_nome_invalid_data(service):
    cliente_service, mock_repository = service
    with pytest.raises(ValidationException):
        cliente_service.select_cliente_by_nome(nome=5)


def test_select_all_clientes(service):
    cliente_service, mock_repository = service

    mock_repository.select_all_clientes.return_value = generate_clientes(2)

    clientes = cliente_service.select_all_clientes()

    mock_repository.select_all_clientes.assert_called_once()

    assert isinstance(clientes, list)
    assert all(isinstance(cliente, ClienteModel) for cliente in clientes)
    assert len(clientes) == 2

    clientes_response = generate_clientes(2)
    for i, cliente in enumerate(clientes):
        assert compare_dicts(cliente.__dict__, clientes_response[i].__dict__)


def test_update_cliente(service):
    cliente_service, mock_repository = service
    cliente_data = generate_clientes_without_id(1)[0].__dict__
    cliente_id = 1

    assert (
        cliente_service.update_cliente(data=cliente_data, cliente_id=cliente_id) is None
    )

    mock_repository.update_cliente(cliente_id=cliente_id, data=cliente_data)

    assert compare_dicts(cliente_data, generate_clientes_without_id(1)[0].__dict__)


def test_update_cliente_invalid_data(service):
    cliente_service, mock_repository = service
    cliente_data = generate_clientes_without_id(1)[0]
    cliente_data.telefone = ""
    with pytest.raises(ValidationException):
        cliente_service.update_cliente(data=cliente_data, cliente_id=1)


def test_delete_cliente(service):
    cliente_service, mock_repository = service
    cliente_id = 1

    assert cliente_service.delete_cliente(cliente_id=cliente_id) is None

    mock_repository.delete_cliente.assert_called_once()
