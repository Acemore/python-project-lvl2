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
    indent = depth * EMPTY_INDENT

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


def get_formated_str(node, depth, key):  # noqa: C901
    status = node[STATE]
    indent = depth * EMPTY_INDENT
    result = []

    if status == ADDED:
        value = node[VALUE]
        result.append(
            (f'{indent}{ADDED_ITEM_INDENT}{key}: '
             f'{format_value(value, depth)}')
        )
    elif status == REMOVED:
        value = node[VALUE]
        result.append(
            (f'{indent}{REMOVED_ITEMS_INDENT}{key}: '
             f'{format_value(value, depth)}')
        )
    elif status == SAME:
        value = node[VALUE]
        result.append(
            (f'{indent}{EMPTY_INDENT}{key}: '
             f'{format_value(value, depth)}')
        )
    elif status == CHANGED:
        first_value = node[FIRST_VALUE]
        second_value = node[SECOND_VALUE]

        result.append(
            (f'{indent}{REMOVED_ITEMS_INDENT}{key}: '
             f'{format_value(first_value, depth)}\n'
             f'{indent}{ADDED_ITEM_INDENT}{key}: '
             f'{format_value(second_value, depth)}')
        )
    elif status == NESTED:
        children = node[CHILDREN]
        nested_indent = (depth + 1) * EMPTY_INDENT

        result.append(f'{nested_indent}{key}: {OPENING_CURLY_BRACKET}')
        for key, value in children.items():
            result.append(get_formated_str(value, depth + 1, key))
        result.append(f'{nested_indent}{CLOSING_CURLY_BRACKET}')

    return LINE_BREAK.join(result)


def format_stylish(diff):
    result = [OPENING_CURLY_BRACKET]

    keys = diff.keys()
    for key in keys:
        node = diff[key]
        depth = 0

        result.append(get_formated_str(node, depth, key))

    result.append(f'{CLOSING_CURLY_BRACKET}')

    return LINE_BREAK.join(result)
