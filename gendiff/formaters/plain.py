import json


def format_value(value):
    if type(value) is int:
        return value
    if value in [False, None, True]:
        return json.dumps(value)
    if type(value) is str:
        return f"'{value}'"
    return '[complex value]'


def get_formated_str(diff, status, key, path):
    path += key

    if status == 'removed':
        return f"Property '{path}' was removed"
    elif status == 'added':
        return (f"Property '{path}' was added with value: "
                f"{format_value(diff[key]['value'])}")
    elif status == 'changed':
        return (f"Property '{path}' was updated. "
                f"From {format_value(diff[key]['first_value'])} "
                f"to {format_value(diff[key]['second_value'])}")
    elif status == 'nested':
        path += '.'
        return format_plain(diff[key]["children"], path)


def format_plain(diff, path=''):
    result = []

    keys = sorted(diff.keys())
    for key in keys:
        status = diff[key]['state']

        str = get_formated_str(diff, status, key, path)
        if str:
            result.append(str)

    return '\n'.join(result)
