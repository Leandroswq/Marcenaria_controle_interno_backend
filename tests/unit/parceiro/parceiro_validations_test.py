import pytest
from src.errors.http_erros import ValidationException
from src.validation.parceiro_validations import (
    validate_parceiro,
    validate_parceiro_optional_fields,
)


# Funções de teste para validate_parceiro


def test_validate_parceiro_valid_data():
    data = {
        "id": 1,
        "nome": "John",
        "empresa": "ABC Company",
        "e_empresa": True,
        "telefone": "12345678901",
    }
    result = validate_parceiro(data)
    assert result is True


def test_validate_parceiro_invalid_data():
    data = {
        "nome": "John",
        "empresa": "ABC Company",
        "e_empresa": True,
        "telefone": "12345678901",
    }

    for key in data.keys():
        test_data = data.copy()
        test_data.pop(key)

        with pytest.raises(ValidationException):
            validate_parceiro(test_data)


def test_validate_parceiro_invalid_id():
    data = {
        "id": "invalid_id",
        "nome": "John",
        "empresa": "ABC Company",
        "e_empresa": True,
        "telefone": "12345678901",
    }
    with pytest.raises(ValidationException):
        validate_parceiro(data)


def test_validate_parceiro_invalid_telefone():
    data = {
        "id": 1,
        "nome": "John",
        "empresa": "ABC Company",
        "e_empresa": True,
        "telefone": "123",
    }
    with pytest.raises(ValidationException):
        validate_parceiro(data)


# Funções de teste para validate_parceiro_optional_fields


def test_validate_parceiro_optional_fields_valid_data():
    data = {
        "id": 1,
        "nome": "John",
        "empresa": "ABC Company",
        "e_empresa": True,
        "telefone": "12345678901",
    }
    result = validate_parceiro_optional_fields(data)
    assert result is True


def test_validate_parceiro_optional_fields_invalid_id():
    data = {
        "id": "invalid_id",
        "nome": "John",
        "empresa": "ABC Company",
        "e_empresa": True,
        "telefone": "12345678901",
    }
    with pytest.raises(ValidationException):
        validate_parceiro_optional_fields(data)


def test_validate_parceiro_optional_fields_invalid_telefone():
    data = {
        "id": 1,
        "nome": "John",
        "empresa": "ABC Company",
        "e_empresa": True,
        "telefone": "123",
    }
    with pytest.raises(ValidationException):
        validate_parceiro_optional_fields(data)
