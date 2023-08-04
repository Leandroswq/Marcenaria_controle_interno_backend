from src.errors.http_erros import ValidationException
from src.validation.common_validations import dict_len_validate, string_validate
import pytest


#  dict_len_validate
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


# string_validate
def test_string_validate_valid_input():
    input_data = "Hello, world!"
    assert string_validate(input_data) is True


def test_string_validate_empty_input():
    input_data = ""
    with pytest.raises(ValidationException):
        string_validate(input_data)


def test_string_validate_long_input():
    input_data = "ssssssssss"
    with pytest.raises(ValidationException):
        string_validate(input_data, max_len=2)


def test_string_validate_non_string_input():
    input_data = 123
    with pytest.raises(ValidationException):
        string_validate(input_data)
