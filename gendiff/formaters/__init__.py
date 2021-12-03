from gendiff.formaters.plain import format_plain
from gendiff.formaters.stylish import format_stylish


formaters = {
    'plain': format_plain,
    'stylish': format_stylish
}


def select_formater(format):
    return formaters[format]
