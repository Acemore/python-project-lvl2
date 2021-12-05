import pytest
from gendiff import generate_diff


@pytest.fixture
def first_json_file_path():
    return 'tests/fixtures/first_nested.yaml'


@pytest.fixture
def second_json_file_path():
    return 'tests/fixtures/second_nested.yml'


@pytest.fixture
def expected_string():
    return open('tests/fixtures/expected_json.txt').read()


def test_generate_diff_with_nested_json(first_json_file_path, second_json_file_path, expected_string):
    assert generate_diff(first_json_file_path, second_json_file_path, "json") == expected_string
