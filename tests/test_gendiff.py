import pytest
from gendiff import generate_diff
from gendiff.formaters import JSON, PLAIN, STYLISH


EXPECTED_FLAT = 'tests/fixtures/expected_flat.txt'
EXPECTED_JSON = 'tests/fixtures/expected_json.txt'
EXPECTED_NESTED = 'tests/fixtures/expected_nested.txt'
EXPECTED_PLAIN = 'tests/fixtures/expected_plain.txt'
FIRST_FLAT_JSON = 'tests/fixtures/first_flat.json'
FIRST_FLAT_YAML = 'tests/fixtures/first_flat.yml'
FIRST_NESTED_JSON = 'tests/fixtures/first_nested.json'
FIRST_NESTED_YAML = 'tests/fixtures/first_nested.yaml'
SECOND_FLAT_JSON = 'tests/fixtures/second_flat.json'
SECOND_FLAT_YAML = 'tests/fixtures/second_flat.yaml'
SECOND_NESTED_JSON = 'tests/fixtures/second_nested.json'
SECOND_NESTED_YAML = 'tests/fixtures/second_nested.yml'


def get_expected_string(file_path):
    with open(file_path) as expected:
        return expected.read()


@pytest.mark.parametrize(
    "first_file_path, second_file_path, format, expected_file_path",
    [
        (FIRST_FLAT_JSON, SECOND_FLAT_JSON, STYLISH, EXPECTED_FLAT),
        (FIRST_FLAT_YAML, SECOND_FLAT_YAML, STYLISH, EXPECTED_FLAT),
        (FIRST_NESTED_JSON, SECOND_NESTED_JSON, STYLISH, EXPECTED_NESTED),
        (FIRST_NESTED_YAML, SECOND_NESTED_YAML, STYLISH, EXPECTED_NESTED),
        (FIRST_NESTED_JSON, SECOND_NESTED_JSON, PLAIN, EXPECTED_PLAIN),
        (FIRST_NESTED_YAML, SECOND_NESTED_YAML, PLAIN, EXPECTED_PLAIN),
        (FIRST_NESTED_JSON, SECOND_NESTED_JSON, JSON, EXPECTED_JSON),
        (FIRST_NESTED_YAML, SECOND_NESTED_YAML, JSON, EXPECTED_JSON)
    ]
)
def test_generate_diff(first_file_path, second_file_path, format, expected_file_path):
    assert generate_diff(
        first_file_path,
        second_file_path,
        format
     ) == get_expected_string(expected_file_path)
