import pytest
from gendiff import generate_diff


@pytest.fixture
def first_yaml_file_path():
    return 'tests/fixtures/file1.yml'


@pytest.fixture
def second_yaml_file_path():
    return 'tests/fixtures/file2.yaml'


@pytest.fixture
def expected_string():
    return open('tests/fixtures/expected_flat.txt').read()


def test_generate_diff_with_yaml(first_yaml_file_path, second_yaml_file_path, expected_string):
    assert generate_diff(first_yaml_file_path, second_yaml_file_path) == expected_string
