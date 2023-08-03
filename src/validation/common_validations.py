from cerberus import Validator
from src.errors.http_erros import ValidationException


def dict_len_validate(data: dict, min_len: int = 1, type_schema="Body"):
    schema = {
        type_schema: {
            "type": "dict",
            "minlength": min_len,  # Mínimo de pares chave-valor requeridos
        }
    }
    validator = Validator(schema)
    response = validator.validate({type_schema: data})

    if response is False:
        raise ValidationException()

    return True
