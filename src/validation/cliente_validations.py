from cerberus import Validator
from src.errors.http_erros import ValidationException
from src.validation.common_validations import dict_len_validate


def validate_cliente(data: dict, id_is_required=False):
    schema = {
        "id": {"type": "integer", "required": id_is_required},
        "nome": {"type": "string", "maxlength": 50, "required": True},
        "sobre_nome": {"type": "string", "maxlength": 100, "required": False},
        "telefone": {"type": "string", "regex": "^[0-9]{11}$", "required": True},
        "empresa": {"type": "string", "maxlength": 50, "required": False},
        "e_empresa": {"type": "boolean", "required": True},
    }

    validator = Validator(schema)
    response = validator.validate(data)

    if response is False:
        raise ValidationException()

    return True


def validate_cliente_optional_fields(data: dict):
    dict_len_validate(data)

    schema = {
        "id": {"type": "integer", "required": False},
        "nome": {"type": "string", "maxlength": 50, "required": False},
        "sobre_nome": {"type": "string", "maxlength": 100, "required": False},
        "telefone": {"type": "string", "regex": "^[0-9]{11}$", "required": False},
        "empresa": {"type": "string", "maxlength": 50, "required": False},
        "e_empresa": {"type": "boolean", "required": False},
    }

    validator = Validator(schema)
    response = validator.validate(data)
    print(validator.errors, "=============")
    print(data)
    if response is False:
        raise ValidationException()

    return True
