import json
from gendiff.search_diff import (
    ADDED, CHANGED, CHILDREN, FIRST_VALUE,
    NESTED, REMOVED, SECOND_VALUE, STATE, VALUE
)


COMPLEX_VALUE = "[complex value]"
DOT = "."
LINE_BREAK = "\n"


def format_value(value):
    if type(value) is int:
        return value
    if value in [False, None, True]:
        return json.dumps(value)
    if type(value) is str:
        return f"'{value}'"
    return COMPLEX_VALUE


def get_formated_str(node, key, path):
    status = node[STATE]
    path += key

    if status == REMOVED:
        return f"Property '{path}' was removed"
    elif status == ADDED:
        return (f"Property '{path}' was added with value: "
                f"{format_value(node[VALUE])}")
    elif status == CHANGED:
        return (f"Property '{path}' was updated. "
                f"From {format_value(node[FIRST_VALUE])} "
                f"to {format_value(node[SECOND_VALUE])}")
    elif status == NESTED:
        path += DOT
        return format_plain(node[CHILDREN], path)


def format_plain(diff, path=''):
    result = []

    keys = diff.keys()
    for key in keys:
        node = diff[key]

        str = get_formated_str(node, key, path)
        if str:
            result.append(str)

    return LINE_BREAK.join(result)
