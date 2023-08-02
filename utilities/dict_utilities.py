def compare_dicts(dict1: dict, dict2: dict):
    response = True
    try:
        for key, value in dict1.items():
            if dict1[key] != dict2[key]:
                response = False
                break
    except KeyError:
        response = False

    return response
