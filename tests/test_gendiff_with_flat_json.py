import pytest
from gendiff import generate_diff


@pytest.fixture
def first_json_file_path():
    return 'tests/fixtures/first_flat.json'


@pytest.fixture
def second_json_file_path():
    return 'tests/fixtures/second_flat.json'


@pytest.fixture
def expected_string():
    return open('tests/fixtures/expected_flat.txt').read()


def test_generate_diff_with_flat_json(first_json_file_path, second_json_file_path, expected_string):
    assert generate_diff(first_json_file_path, second_json_file_path) == expected_string
