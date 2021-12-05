from gendiff.search_diff import search_diff
from gendiff.file_type_parser import get_file_content
from gendiff.formaters.json import format_json
from gendiff.formaters.plain import format_plain
from gendiff.formaters.stylish import format_stylish


JSON = "json"
PLAIN = "plain"
STYLISH = "stylish"


def generate_diff(first_file_path, second_file_path, format=STYLISH):
    first_file = get_file_content(first_file_path)
    second_file = get_file_content(second_file_path)

    diff = search_diff(first_file, second_file)

    if format == JSON:
        return format_json(diff)
    if format == PLAIN:
        return format_plain(diff)
    return format_stylish(diff)
