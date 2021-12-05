from gendiff.formaters import (
    ADDED, CHANGED, CHILDREN, FIRST_VALUE, NESTED,
    REMOVED, SAME, STATE, SECOND_VALUE, VALUE
)


def get_keys(file):
    return set(file.keys())


def get_dict(state, first_data_key, first_data_value):
    return {
        STATE: state,
        first_data_key: first_data_value
    }


def get_dict_for_changed_items(state, first_data_key, first_data_value,
                               second_data_key, second_data_value):
    result_dict = get_dict(state, first_data_key, first_data_value)
    result_dict[second_data_key] = second_data_value
    return result_dict


def get_value(first_dict, second_dict, key):
    first_dict_key_value = first_dict.get(key)
    second_dict_key_value = second_dict.get(key)

    if type(first_dict_key_value) is dict and (
        type(second_dict_key_value) is dict
    ):
        return get_dict(
            NESTED,
            CHILDREN,
            search_diff(first_dict_key_value, second_dict_key_value)
        )
    elif first_dict_key_value == second_dict_key_value:
        return get_dict(SAME, VALUE, first_dict_key_value)
    elif key in get_keys(first_dict) and key not in get_keys(second_dict):
        return get_dict(REMOVED, VALUE, first_dict_key_value)
    elif key not in get_keys(first_dict) and key in get_keys(second_dict):
        return get_dict(ADDED, VALUE, second_dict_key_value)
    else:
        return get_dict_for_changed_items(
            CHANGED,
            FIRST_VALUE,
            first_dict_key_value,
            SECOND_VALUE,
            second_dict_key_value
        )


def search_diff(first_dict, second_dict):
    diff = {}

    all_keys = sorted(get_keys(first_dict).union(get_keys(second_dict)))
    for key in all_keys:
        diff[key] = get_value(first_dict, second_dict, key)

    return diff
