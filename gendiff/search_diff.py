ADDED = "added"
CHANGED = "changed"
CHILDREN = "children"
FIRST_VALUE = "first_value"
NESTED = "nested"
REMOVED = "removed"
SAME = "same"
SECOND_VALUE = "second_value"
STATE = "state"
VALUE = "value"


def get_keys(file):
    return set(file.keys())


def get_value(first_dict, second_dict, key):
    first_dict_key_value = first_dict.get(key)
    second_dict_key_value = second_dict.get(key)

    if type(first_dict_key_value) is dict and (
        type(second_dict_key_value) is dict
    ):
        return {
            STATE: NESTED,
            CHILDREN: search_diff(first_dict_key_value, second_dict_key_value)
        }
    elif first_dict_key_value == second_dict_key_value:
        return {
            STATE: SAME,
            VALUE: first_dict_key_value
        }
    elif key in get_keys(first_dict) and key not in get_keys(second_dict):
        return {
            STATE: REMOVED,
            VALUE: first_dict_key_value
        }
    elif key not in get_keys(first_dict) and key in get_keys(second_dict):
        return {
            STATE: ADDED,
            VALUE: second_dict_key_value
        }
    else:
        return {
            STATE: CHANGED,
            FIRST_VALUE: first_dict_key_value,
            SECOND_VALUE: second_dict_key_value
        }


def search_diff(first_dict, second_dict):
    diff = {}

    all_keys = sorted(get_keys(first_dict).union(get_keys(second_dict)))
    for key in all_keys:
        diff[key] = get_value(first_dict, second_dict, key)

    return diff
