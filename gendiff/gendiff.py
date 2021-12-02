from gendiff.search_diff import search_diff
from gendiff.file_type_parser import get_file_content
from gendiff.formaters import select_formater


def generate_diff(first_file_path, second_file_path, format='stylish'):
    first_file = get_file_content(first_file_path)
    second_file = get_file_content(second_file_path)

    diff = search_diff(first_file, second_file)
    return select_formater(format)(diff)
