from src.errors.http_erros import ValidationException
from src.validation.common_validations import dict_len_validate
import pytest


def test_dict_len_validate():
    data = {"key1": "value1", "key2": "value2"}
    result = dict_len_validate(data)
    assert result is True

    data = {"key1": "value1"}
    with pytest.raises(ValidationException):
        dict_len_validate(data, min_len=2)

    data = {}
    with pytest.raises(ValidationException):
        dict_len_validate(data)
