from gendiff.formaters.stylish import format_stylish


formaters = {
    'stylish': format_stylish
}


def select_formater(format):
    return formaters[format]
