import json
from gendiff.file_type_parser import get_file_content


ADDED_PREFIX = '+ '
FINISH_SUBSTR = '\n}'
SEP = '\n  '
REMOVED_PREFIX = '- '
SAME_PREFIX = '  '
START_SUBSTR = '{\n  '


def add_substr(substrs, file, key, prefix):
    substrs.append(
        get_result_substr(
            prefix,
            key,
            get_value(file, key)
        )
    )


def get_keys(file):
    return set(file.keys())


def get_result_substr(prefix, key, value):
    return f'{prefix}{key}: {value}'


def get_value(file, key):
    value = file.get(key)
    return json.dumps(value) if value in [True, False, None] else value


def is_same_item(key, first_file, second_file):
    return first_file.get(key) == second_file.get(key)


def generate_diff(first_file_path, second_file_path):
    first_file = get_file_content(first_file_path)
    second_file = get_file_content(second_file_path)

    first_file_keys = get_keys(first_file)
    second_file_keys = get_keys(second_file)
    all_keys = first_file_keys.union(second_file_keys)

    result = []

    for key in all_keys:
        if is_same_item(key, first_file, second_file):
            add_substr(result, first_file, key, SAME_PREFIX)
        else:
            if key in first_file_keys:
                add_substr(result, first_file, key, REMOVED_PREFIX)
            if key in second_file_keys:
                add_substr(result, second_file, key, ADDED_PREFIX)

    return START_SUBSTR + (
        SEP.join(sorted(result, key=lambda str: str[2]))
    ) + FINISH_SUBSTR
