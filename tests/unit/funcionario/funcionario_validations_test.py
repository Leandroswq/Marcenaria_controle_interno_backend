import pytest
from src.errors.http_erros import ValidationException
from src.validation.funcionario_validations import (
    validate_funcionario,
    validate_funcionario_optional_fields,
)

# Funções de teste para validate_funcionario


def test_validate_funcionario_valid_data():
    data = {"id": 1, "nome": "John", "funcao": "Manager", "telefone": "12345678901"}
    result = validate_funcionario(data)
    assert result is True


def test_validate_funcionario_invalid_data():
    data = {"nome": "John", "funcao": "Manager", "telefone": "12345678901"}

    for key in data.keys():
        test_data = data.copy()
        test_data.pop(key)

        with pytest.raises(ValidationException):
            validate_funcionario(test_data)


def test_validate_funcionario_invalid_id():
    data = {
        "id": "invalid_id",
        "nome": "John",
        "funcao": "Manager",
        "telefone": "12345678901",
    }
    with pytest.raises(ValidationException):
        validate_funcionario(data)


def test_validate_funcionario_invalid_telefone():
    data = {
        "id": 1,
        "nome": "John",
        "funcao": "Manager",
        "telefone": "123",
    }
    with pytest.raises(ValidationException):
        validate_funcionario(data)


# Funções de teste para validate_funcionario_optional_fields


def test_validate_funcionario_optional_fields_valid_data():
    data = {"id": 1, "nome": "John", "funcao": "Manager", "telefone": "12345678901"}
    result = validate_funcionario_optional_fields(data)
    assert result is True


def test_validate_funcionario_optional_fields_invalid_id():
    data = {
        "id": "invalid_id",
        "nome": "John",
        "funcao": "Manager",
        "telefone": "12345678901",
    }
    with pytest.raises(ValidationException):
        validate_funcionario_optional_fields(data)


def test_validate_funcionario_optional_fields_invalid_telefone():
    data = {
        "id": 1,
        "nome": "John",
        "funcao": "Manager",
        "telefone": "123",
    }
    with pytest.raises(ValidationException):
        validate_funcionario_optional_fields(data)
