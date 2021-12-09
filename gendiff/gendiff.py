from gendiff.file_parser import parse_file
from gendiff.formaters import STYLISH, select_format
from gendiff.search_diff import search_diff


def generate_diff(first_file_path, second_file_path, format=STYLISH):
    first_file = parse_file(first_file_path)
    second_file = parse_file(second_file_path)

    diff = search_diff(first_file, second_file)

    return select_format(format)(diff)
