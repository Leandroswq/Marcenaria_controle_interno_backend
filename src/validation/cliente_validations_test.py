import pytest
from src.errors.http_erros import ValidationException
from src.validation.cliente_validations import (
    validate_cliente,
    validate_cliente_optional_fields,
)

# Funções de teste para validate_cliente


def test_validate_cliente_valid_data():
    data = {"id": 1, "nome": "John", "telefone": "12345678901", "e_empresa": True}
    result = validate_cliente(data)
    assert result is True


def test_validate_cliente_invalid_data():
    data = {"nome": "John", "telefone": "12345678901", "e_empresa": True}

    for key in data.keys():
        test_data = data.copy()
        test_data.pop(key)

        with pytest.raises(ValidationException) as exc_info:
            validate_cliente(test_data)


def test_validate_cliente_invalid_id():
    data = {
        "id": "invalid_id",
        "nome": "John",
        "telefone": "12345678901",
        "e_empresa": True,
    }
    with pytest.raises(ValidationException):
        validate_cliente(data)


def test_validate_cliente_invalid_telefone():
    data = {
        "id": 1,
        "nome": "John",
        "telefone": "123",
        "e_empresa": True,
    }
    with pytest.raises(ValidationException):
        validate_cliente(data)


def test_validate_cliente_invalid_e_empresa():
    data = {
        "id": 1,
        "nome": "John",
        "telefone": "12345678901",
        "e_empresa": "True",
    }
    with pytest.raises(ValidationException):
        validate_cliente(data)


# Funções de teste para validate_cliente_optional_fields


def test_validate_cliente_optional_fields_valid_data():
    data = {"id": 1, "nome": "John", "telefone": "12345678901", "e_empresa": True}
    result = validate_cliente_optional_fields(data)
    assert result is True


def test_validate_cliente_optional_fields_invalid_id():
    data = {
        "id": "invalid_id",
        "nome": "John",
        "telefone": "12345678901",
        "e_empresa": True,
    }
    with pytest.raises(ValidationException):
        validate_cliente_optional_fields(data)


def test_validate_cliente_optional_fields_invalid_telefone():
    data = {
        "id": 1,
        "nome": "John",
        "telefone": "123",
        "e_empresa": True,
    }
    with pytest.raises(ValidationException):
        validate_cliente_optional_fields(data)


def test_validate_cliente_optional_fields_invalid_e_empresa():
    data = {
        "id": 1,
        "nome": "John",
        "telefone": "12345678901",
        "e_empresa": "True",
    }
    with pytest.raises(ValidationException):
        validate_cliente_optional_fields(data)
