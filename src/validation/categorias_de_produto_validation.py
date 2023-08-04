from cerberus import Validator
from src.errors.http_erros import ValidationException
from src.validation.common_validations import dict_len_validate


def validate_categoria_de_produto(data: dict, categoria_id_is_required=False):
    schema = {
        "categoria_id": {"type": "integer", "required": categoria_id_is_required},
        "categoria": {
            "type": "string",
            "maxlength": 50,
            "required": True,
            "minlength": 3,
        },
    }

    validator = Validator(schema)
    response = validator.validate(data)

    if response is False:
        raise ValidationException()

    return True


def validate_categoria_de_produto_optional_fields(data: dict):
    dict_len_validate(data)

    schema = {
        "categoria_id": {"type": "integer", "required": False},
        "categoria": {
            "type": "string",
            "maxlength": 50,
            "required": False,
            "minlength": 3,
        },
    }

    validator = Validator(schema)
    response = validator.validate(data)

    if response is False:
        raise ValidationException()

    return True
