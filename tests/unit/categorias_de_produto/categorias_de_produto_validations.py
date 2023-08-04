import pytest
from src.errors.http_erros import ValidationException
from src.validation.categorias_de_produto_validation import (
    validate_categoria_de_produto,
    validate_categoria_de_produto_optional_fields,
)

# Funções de teste para validate_categoria_de_produto


def test_validate_categoria_de_produto_valid_data():
    data = {"categoria_id": 1, "categoria": "Eletrônicos"}
    result = validate_categoria_de_produto(data)
    assert result is True


def test_validate_categoria_de_produto_invalid_data():
    data = {"categoria": "Eletrônicos"}

    for key in data.keys():
        test_data = data.copy()
        test_data.pop(key)

        with pytest.raises(ValidationException):
            validate_categoria_de_produto(test_data)


def test_validate_categoria_de_produto_invalid_categoria_id():
    data = {
        "categoria_id": "invalid_id",
        "categoria": "Eletrônicos",
    }
    with pytest.raises(ValidationException):
        validate_categoria_de_produto(data)


def test_validate_categoria_de_produto_invalid_categoria():
    data = {
        "categoria_id": 1,
        "categoria": "",
    }
    with pytest.raises(ValidationException):
        validate_categoria_de_produto(data)


# Funções de teste para validate_categoria_de_produto_optional_fields


def test_validate_categoria_de_produto_optional_fields_valid_data():
    data = {"categoria_id": 1, "categoria": "Eletrônicos"}
    result = validate_categoria_de_produto_optional_fields(data)
    assert result is True


def test_validate_categoria_de_produto_optional_fields_invalid_categoria_id():
    data = {
        "categoria_id": "invalid_id",
        "categoria": "Eletrônicos",
    }
    with pytest.raises(ValidationException):
        validate_categoria_de_produto_optional_fields(data)


def test_validate_categoria_de_produto_optional_fields_invalid_categoria():
    data = {
        "categoria_id": 1,
        "categoria": "",
    }
    with pytest.raises(ValidationException):
        validate_categoria_de_produto_optional_fields(data)
