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


def convert_dict_to_str(dict_, depth):
    nested_diff = []
    indent = EMPTY_INDENT * depth

    if type(dict_) is dict:
        nested_diff.append(OPENING_CURLY_BRACKET)

        keys = dict_.keys()
        for key in keys:
            str = (f'{indent}{EMPTY_INDENT}{key}: '
                   f'{convert_dict_to_str(dict_[key], depth + 1)}')
            nested_diff.append(str)

        nested_diff.append(f'{indent}{CLOSING_CURLY_BRACKET}')
    else:
        str = format_value(dict_, depth)
        nested_diff.append(str)

    return LINE_BREAK.join(nested_diff)


def format_value(value, depth):
    if value in [False, None, True]:
        return json.dumps(value)
    elif type(value) is dict:
        return convert_dict_to_str(value, depth + 1)
    return str(value)


def get_formated_str(node, depth, indent, key):
    status = node[STATE]

    if status == ADDED:
        value = node[VALUE]
        return (f'{indent}{ADDED_ITEM_INDENT}{key}: '
                f'{format_value(value, depth)}')
    elif status == REMOVED:
        value = node[VALUE]
        return (f'{indent}{REMOVED_ITEMS_INDENT}{key}: '
                f'{format_value(value, depth)}')
    elif status == SAME:
        value = node[VALUE]
        return (f'{indent}{EMPTY_INDENT}{key}: '
                f'{format_value(value, depth)}')
    elif status == CHANGED:
        first_value = node[FIRST_VALUE]
        second_value = node[SECOND_VALUE]
        return (f'{indent}{REMOVED_ITEMS_INDENT}{key}: '
                f'{format_value(first_value, depth)}\n'
                f'{indent}{ADDED_ITEM_INDENT}{key}: '
                f'{format_value(second_value, depth)}')
    elif status == NESTED:
        children = node[CHILDREN]
        return (f'{indent}{EMPTY_INDENT}{key}: '
                f'{format_stylish(children, depth + 1)}')


def format_stylish(diff, depth=0):
    result = [OPENING_CURLY_BRACKET]
    indent = EMPTY_INDENT * depth

    keys = diff.keys()
    for key in keys:
        node = diff[key]

        str = get_formated_str(node, depth, indent, key)
        result.append(str)

    result.append(f'{indent}{CLOSING_CURLY_BRACKET}')

    return LINE_BREAK.join(result)
