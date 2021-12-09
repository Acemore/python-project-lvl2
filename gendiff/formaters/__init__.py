from gendiff.formaters.json import format_json
from gendiff.formaters.plain import format_plain
from gendiff.formaters.stylish import format_stylish


JSON = "json"
PLAIN = "plain"
STYLISH = "stylish"

FORMATS = {
    JSON: format_json,
    PLAIN: format_plain,
    STYLISH: format_stylish,
}


def select_format(format):
    return FORMATS[format]
