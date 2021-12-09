import json
from gendiff.search_diff import (
    ADDED, CHANGED, CHILDREN, FIRST_VALUE, NESTED,
    REMOVED, SAME, SECOND_VALUE, STATE, VALUE
)


ADDED_ITEM_INDENT = "  + "
CLOSING_CURLY_BRACKET = "}"
EMPTY_INDENT = "    "
LINE_BREAK = "\n"
OPENING_CURLY_BRACKET = "{"
REMOVED_ITEMS_INDENT = "  - "


def get_dict_str(diff, depth):
    nested_diff = []
    indent = EMPTY_INDENT * depth

    if type(diff) is dict:
        nested_diff.append(OPENING_CURLY_BRACKET)

        keys = diff.keys()
        for key in keys:
            str = (f'{indent}{EMPTY_INDENT}{key}: '
                   f'{get_dict_str(diff[key], depth + 1)}')
            nested_diff.append(str)

        nested_diff.append(f'{indent}{CLOSING_CURLY_BRACKET}')
    else:
        str = format_value(diff, depth)
        nested_diff.append(str)

    return LINE_BREAK.join(nested_diff)


def format_value(value, depth):
    if value in [False, None, True]:
        return json.dumps(value)
    elif type(value) is dict:
        return get_dict_str(value, depth + 1)
    return str(value)


def get_formated_str(diff, depth, indent, status, key):
    if status == ADDED:
        return (f'{indent}{ADDED_ITEM_INDENT}{key}: '
                f'{format_value(diff[key][VALUE], depth)}')
    elif status == REMOVED:
        return (f'{indent}{REMOVED_ITEMS_INDENT}{key}: '
                f'{format_value(diff[key][VALUE], depth)}')
    elif status == SAME:
        return (f'{indent}{EMPTY_INDENT}{key}: '
                f'{format_value(diff[key][VALUE], depth)}')
    elif status == CHANGED:
        return (f'{indent}{REMOVED_ITEMS_INDENT}{key}: '
                f'{format_value(diff[key][FIRST_VALUE], depth)}\n'
                f'{indent}{ADDED_ITEM_INDENT}{key}: '
                f'{format_value(diff[key][SECOND_VALUE], depth)}')
    elif status == NESTED:
        return (f'{indent}{EMPTY_INDENT}{key}: '
                f'{format_stylish(diff[key][CHILDREN], depth + 1)}')


def format_stylish(diff, depth=0):
    result = [OPENING_CURLY_BRACKET]
    indent = EMPTY_INDENT * depth

    keys = diff.keys()
    for key in keys:
        status = diff[key][STATE]

        str = get_formated_str(diff, depth, indent, status, key)
        result.append(str)

    result.append(f'{indent}{CLOSING_CURLY_BRACKET}')

    return LINE_BREAK.join(result)
