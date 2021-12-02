import json


STATES = {
    'added': '  + ',
    'nested': '    ',
    'removed': '  - ',
    'same': '    '
}


def get_dict_str(diff, depth):
    nested_diff = []
    indent = '    ' * depth

    if type(diff) is dict:
        nested_diff.append('{')

        keys = diff.keys()
        for key in keys:
            str = (f'{indent}{STATES["same"]}{key}: '
                   f'{get_dict_str(diff[key], depth + 1)}')
            nested_diff.append(str)

        nested_diff.append(f'{indent}}}')
    else:
        str = format_value(diff, depth)
        nested_diff.append(str)

    return '\n'.join(nested_diff)


def format_value(value, depth):
    if value in [False, None, True]:
        return json.dumps(value)
    elif type(value) is dict:
        return get_dict_str(value, depth + 1)
    return str(value)


def get_formated_str(diff, depth, indent, status, key):
    if status == 'added':
        return (f'{indent}{STATES["added"]}{key}: '
                f'{format_value(diff[key]["value"], depth)}')
    elif status == 'removed':
        return (f'{indent}{STATES["removed"]}{key}: '
                f'{format_value(diff[key]["value"], depth)}')
    elif status == 'same':
        return (f'{indent}{STATES["same"]}{key}: '
                f'{format_value(diff[key]["value"], depth)}')
    elif status == 'changed':
        return (f'{indent}{STATES["removed"]}{key}: '
                f'{format_value(diff[key]["first_value"], depth)}\n'
                f'{indent}{STATES["added"]}{key}: '
                f'{format_value(diff[key]["second_value"], depth)}')
    elif status == 'nested':
        return (f'{indent}{STATES["nested"]}{key}: '
                f'{format_stylish(diff[key]["children"], depth + 1)}')


def format_stylish(diff, depth=0):
    result = ['{']
    indent = '    ' * depth

    keys = sorted(diff.keys())
    for key in keys:
        status = diff[key]['state']

        str = get_formated_str(diff, depth, indent, status, key)
        result.append(str)

    result.append(f'{indent}}}')

    return '\n'.join(result)
