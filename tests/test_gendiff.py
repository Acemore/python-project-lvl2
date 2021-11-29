import pytest
from gendiff import generate_diff


@pytest.fixture
def first_json_file_path():
    return 'tests/fixtures/file1.json'


@pytest.fixture
def second_json_file_path():
    return 'tests/fixtures/file2.json'


@pytest.fixture
def expected_string():
    return open('tests/fixtures/expected_json.txt').read()


def test_generate_diff(first_json_file_path, second_json_file_path, expected_string):
    assert generate_diff(first_json_file_path, second_json_file_path) == expected_string
