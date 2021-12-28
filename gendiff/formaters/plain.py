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
    result = []

    if status == REMOVED:
        result.append(
            f"Property '{path}' was removed"
        )
    elif status == ADDED:
        value = node[VALUE]

        result.append(
            (f"Property '{path}' was added with value: "
                f"{format_value(value)}")
        )
    elif status == CHANGED:
        first_value = node[FIRST_VALUE]
        second_value = node[SECOND_VALUE]

        result.append(
            (f"Property '{path}' was updated. "
                f"From {format_value(first_value)} "
                f"to {format_value(second_value)}")
        )
    elif status == NESTED:
        children = node[CHILDREN]
        path += DOT

        for key, value in children.items():
            result.append(get_formated_str(value, key, path))

    return LINE_BREAK.join(result)


def format_plain(diff):
    path = ''
    result = []

    keys = diff.keys()
    for key in keys:
        node = diff[key]

        formated_str = get_formated_str(node, key, path)
        if formated_str:
            result.append(formated_str)

    return LINE_BREAK.join(result).replace("\n\n", "\n")
