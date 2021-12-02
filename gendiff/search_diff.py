def get_keys(file):
    return set(file.keys())


def get_value(first_dict, second_dict, key):
    first_dict_key_value = first_dict.get(key)
    second_dict_key_value = second_dict.get(key)

    if isinstance(first_dict_key_value, dict) and (
        isinstance(second_dict_key_value, dict)
    ):
        return {
            'state': 'nested',
            'children': search_diff(first_dict_key_value, second_dict_key_value)
        }
    elif first_dict_key_value == second_dict_key_value:
        return {
            'state': 'same',
            'value': first_dict_key_value
        }
    elif key in get_keys(first_dict) and key not in get_keys(second_dict):
        return {
            'state': 'removed',
            'value': first_dict_key_value
        }
    elif key not in get_keys(first_dict) and key in get_keys(second_dict):
        return {
            'state': 'added',
            'value': second_dict_key_value
        }
    elif not isinstance(first_dict_key_value, dict) or (
        not isinstance(second_dict_key_value, dict)
    ):
        return {
            'state': 'changed',
            'first_value': first_dict_key_value,
            'second_value': second_dict_key_value
        }


def search_diff(first_dict, second_dict):
    diff = {}
    all_keys = get_keys(first_dict).union(get_keys(second_dict))

    for key in all_keys:
        diff[key] = get_value(first_dict, second_dict, key)

    return diff
