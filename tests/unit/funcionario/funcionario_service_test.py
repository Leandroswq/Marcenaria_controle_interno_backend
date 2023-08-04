import pytest
from src.errors.http_erros import ValidationException
from src.services.funcionario_service import FuncionarioService
from src.models.tables.funcionario_models import (
    FuncionarioWithoutIdModel,
    FuncionarioModel,
)
from utilities.dict_utilities import compare_dicts
from tests.unit.funcionario.funcionario_mock import (
    generate_funcionarios,
    generate_funcionarios_without_id,
)


@pytest.fixture
def service_repository(mocker):
    mock_repository = mocker.Mock()
    funcionario_service = FuncionarioService(repository=mock_repository)

    return funcionario_service, mock_repository


def test_insert_funcionario(service_repository):
    funcionario_service, mock_repository = service_repository
    funcionario_data = generate_funcionarios_without_id(1)[0]

    assert funcionario_service.insert_funcionario(data=funcionario_data) is None

    funcionario_data = generate_funcionarios_without_id(1)[0]
    mock_repository.insert_funcionario.assert_called_once_with(
        nome=funcionario_data.nome,
        sobre_nome=funcionario_data.sobre_nome,
        funcao=funcionario_data.funcao,
        telefone=funcionario_data.telefone,
    )


def test_insert_funcionario_invalid_data(service_repository):
    funcionario_service, mock_repository = service_repository
    funcionario_data = generate_funcionarios_without_id(1)[0]
    funcionario_data.telefone = ""
    with pytest.raises(ValidationException):
        funcionario_service.insert_funcionario(data=funcionario_data)


def test_select_funcionario_by_id(service_repository):
    funcionario_service, mock_repository = service_repository
    funcionario_id = 1

    mock_response = generate_funcionarios(1)

    mock_repository.select_funcionario_by_id.return_value = mock_response

    funcionarios = funcionario_service.select_funcionario_by_id(
        funcionario_id=funcionario_id
    )

    mock_repository.select_funcionario_by_id.assert_called_once_with(
        funcionario_id=funcionario_id
    )

    assert isinstance(funcionarios, list)
    assert all(
        isinstance(funcionario, FuncionarioModel) for funcionario in funcionarios
    )
    assert compare_dicts(funcionarios[0].__dict__, generate_funcionarios(1)[0].__dict__)


def test_select_funcionario_by_nome(service_repository):
    funcionario_service, mock_repository = service_repository
    mock_repository.select_funcionario_by_nome.return_value = generate_funcionarios(2)

    nome = "John"
    funcionarios = funcionario_service.select_funcionario_by_nome(nome=nome)

    mock_repository.select_funcionario_by_nome.assert_called_once_with(nome=nome)

    assert isinstance(funcionarios, list)
    assert all(
        isinstance(funcionario, FuncionarioModel) for funcionario in funcionarios
    )
    assert len(funcionarios) == 2

    funcionarios_response = generate_funcionarios(2)

    for i, funcionario in enumerate(funcionarios):
        assert compare_dicts(funcionario.__dict__, funcionarios_response[i].__dict__)


def test_select_funcionario_by_nome_invalid_data(service_repository):
    funcionario_service, mock_repository = service_repository
    with pytest.raises(ValidationException):
        funcionario_service.select_funcionario_by_nome(nome=5)


def test_select_all_funcionarios(service_repository):
    funcionario_service, mock_repository = service_repository

    mock_repository.select_all_funcionarios.return_value = generate_funcionarios(2)

    funcionarios = funcionario_service.select_all_funcionarios()

    mock_repository.select_all_funcionarios.assert_called_once()

    assert isinstance(funcionarios, list)
    assert all(
        isinstance(funcionario, FuncionarioModel) for funcionario in funcionarios
    )
    assert len(funcionarios) == 2

    funcionarios_response = generate_funcionarios(2)
    for i, funcionario in enumerate(funcionarios):
        assert compare_dicts(funcionario.__dict__, funcionarios_response[i].__dict__)


def test_update_funcionario(service_repository):
    funcionario_service, mock_repository = service_repository
    funcionario_data = generate_funcionarios_without_id(1)[0].__dict__
    funcionario_id = 1

    assert (
        funcionario_service.update_funcionario(
            data=funcionario_data, funcionario_id=funcionario_id
        )
        is None
    )

    mock_repository.update_funcionario(
        funcionario_id=funcionario_id, data=funcionario_data
    )

    data = generate_funcionarios_without_id(1)[0].__dict__
    data["id"] = funcionario_id
    assert compare_dicts(funcionario_data, data)


def test_update_funcionario_invalid_data(service_repository):
    funcionario_service, mock_repository = service_repository
    funcionario_data = generate_funcionarios_without_id(1)[0]
    funcionario_data.telefone = ""
    with pytest.raises(ValidationException):
        funcionario_service.update_funcionario(
            data=funcionario_data.__dict__, funcionario_id=1
        )


def test_delete_funcionario(service_repository):
    funcionario_service, mock_repository = service_repository
    funcionario_id = 1

    assert funcionario_service.delete_funcionario(funcionario_id=funcionario_id) is None

    mock_repository.delete_funcionario.assert_called_once()
