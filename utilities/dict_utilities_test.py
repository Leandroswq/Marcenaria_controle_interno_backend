from utilities.dict_utilities import compare_dicts


def test_compare_dicts_equal():
    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {"a": 1, "b": 2, "c": 3}
    assert compare_dicts(dict1, dict2) is True


def test_compare_dicts_not_equal():
    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {"a": 1, "b": 3, "c": 3}
    assert compare_dicts(dict1, dict2) is False


def test_compare_dicts_different_keys():
    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {"a": 1, "b": 2, "d": 3}
    assert compare_dicts(dict1, dict2) is False
