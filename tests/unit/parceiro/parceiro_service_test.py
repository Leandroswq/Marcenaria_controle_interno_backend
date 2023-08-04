import pytest
from src.errors.http_erros import ValidationException
from src.services.parceiro_service import ParceiroService
from src.models.tables.parceiro_models import (
    ParceiroWithoutIdModel,
    ParceiroModel,
)
from utilities.dict_utilities import compare_dicts
from typing import List


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


@pytest.fixture
def service_repository(mocker):
    mock_repository = mocker.Mock()
    parceiro_service = ParceiroService(repository=mock_repository)

    return parceiro_service, mock_repository


def test_insert_parceiro(service_repository):
    parceiro_service, mock_repository = service_repository
    parceiro_data = generate_parceiros_without_id(1)[0]

    assert parceiro_service.insert_parceiro(data=parceiro_data) is None

    parceiro_data = generate_parceiros_without_id(1)[0]
    mock_repository.insert_parceiro.assert_called_once_with(
        nome=parceiro_data.nome,
        sobre_nome=parceiro_data.sobre_nome,
        empresa=parceiro_data.empresa,
        e_empresa=parceiro_data.e_empresa,
        telefone=parceiro_data.telefone,
    )


def test_insert_parceiro_invalid_data(service_repository):
    parceiro_service, mock_repository = service_repository
    parceiro_data = generate_parceiros_without_id(1)[0]
    parceiro_data.telefone = ""
    with pytest.raises(ValidationException):
        parceiro_service.insert_parceiro(data=parceiro_data)


def test_select_parceiro_by_id(service_repository):
    parceiro_service, mock_repository = service_repository
    parceiro_id = 1

    mock_response = generate_parceiros(1)

    mock_repository.select_parceiro_by_id.return_value = mock_response

    parceiros = parceiro_service.select_parceiro_by_id(parceiro_id=parceiro_id)

    mock_repository.select_parceiro_by_id.assert_called_once_with(
        parceiro_id=parceiro_id
    )

    assert isinstance(parceiros, list)
    assert all(isinstance(parceiro, ParceiroModel) for parceiro in parceiros)
    assert compare_dicts(parceiros[0].__dict__, generate_parceiros(1)[0].__dict__)


def test_select_parceiro_by_nome(service_repository):
    parceiro_service, mock_repository = service_repository
    mock_repository.select_parceiro_by_nome.return_value = generate_parceiros(2)

    nome = "John"
    parceiros = parceiro_service.select_parceiro_by_nome(nome=nome)

    mock_repository.select_parceiro_by_nome.assert_called_once_with(nome=nome)

    assert isinstance(parceiros, list)
    assert all(isinstance(parceiro, ParceiroModel) for parceiro in parceiros)
    assert len(parceiros) == 2

    parceiros_response = generate_parceiros(2)

    for i, parceiro in enumerate(parceiros):
        assert compare_dicts(parceiro.__dict__, parceiros_response[i].__dict__)


def test_select_parceiro_by_nome_invalid_data(service_repository):
    parceiro_service, mock_repository = service_repository
    with pytest.raises(ValidationException):
        parceiro_service.select_parceiro_by_nome(nome=5)


def test_select_parceiro_by_id(service_repository):
    parceiro_service, mock_repository = service_repository
    parceiro_id = 1

    mock_response = generate_parceiros(1)

    mock_repository.select_parceiro_by_id.return_value = mock_response

    parceiros = parceiro_service.select_parceiro_by_id(parceiro_id=parceiro_id)

    mock_repository.select_parceiro_by_id.assert_called_once_with(
        parceiro_id=parceiro_id
    )

    assert isinstance(parceiros, list)
    assert all(isinstance(parceiro, ParceiroModel) for parceiro in parceiros)
    assert compare_dicts(parceiros[0].__dict__, generate_parceiros(1)[0].__dict__)


def test_select_parceiro_by_nome(service_repository):
    parceiro_service, mock_repository = service_repository
    mock_repository.select_parceiro_by_nome.return_value = generate_parceiros(2)

    nome = "John"
    parceiros = parceiro_service.select_parceiro_by_nome(nome=nome)

    mock_repository.select_parceiro_by_nome.assert_called_once_with(nome=nome)

    assert isinstance(parceiros, list)
    assert all(isinstance(parceiro, ParceiroModel) for parceiro in parceiros)
    assert len(parceiros) == 2

    parceiros_response = generate_parceiros(2)

    for i, parceiro in enumerate(parceiros):
        assert compare_dicts(parceiro.__dict__, parceiros_response[i].__dict__)


def test_select_parceiro_by_nome_invalid_data(service_repository):
    parceiro_service, mock_repository = service_repository
    with pytest.raises(ValidationException):
        parceiro_service.select_parceiro_by_nome(nome=5)


def test_select_all_parceiros(service_repository):
    parceiro_service, mock_repository = service_repository

    mock_repository.select_all_parceiros.return_value = generate_parceiros(2)

    parceiros = parceiro_service.select_all_parceiros()

    mock_repository.select_all_parceiros.assert_called_once()

    assert isinstance(parceiros, list)
    assert all(isinstance(parceiro, ParceiroModel) for parceiro in parceiros)
    assert len(parceiros) == 2

    parceiros_response = generate_parceiros(2)
    for i, parceiro in enumerate(parceiros):
        assert compare_dicts(parceiro.__dict__, parceiros_response[i].__dict__)


def test_update_parceiro(service_repository):
    parceiro_service, mock_repository = service_repository
    parceiro_data = generate_parceiros_without_id(1)[0].__dict__
    parceiro_id = 1

    assert (
        parceiro_service.update_parceiro(data=parceiro_data, parceiro_id=parceiro_id)
        is None
    )

    mock_repository.update_parceiro(parceiro_id=parceiro_id, data=parceiro_data)

    data = generate_parceiros_without_id(1)[0].__dict__
    data["id"] = parceiro_id
    assert compare_dicts(parceiro_data, data)


def test_update_parceiro_invalid_data(service_repository):
    parceiro_service, mock_repository = service_repository
    parceiro_data = generate_parceiros_without_id(1)[0]
    parceiro_data.telefone = ""
    with pytest.raises(ValidationException):
        parceiro_service.update_parceiro(data=parceiro_data.__dict__, parceiro_id=1)


def test_delete_parceiro(service_repository):
    parceiro_service, mock_repository = service_repository
    parceiro_id = 1

    assert parceiro_service.delete_parceiro(parceiro_id=parceiro_id) is None

    mock_repository.delete_parceiro.assert_called_once()
