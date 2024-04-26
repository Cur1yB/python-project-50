import pytest
from gendiff import generate_diff


@pytest.mark.parametrize("file1, file2, formatter, expected", [
    ("tests/fixtures/file3.json", "tests/fixtures/file4.json", 'plain',
     "tests/fixtures/expected_result_plain.txt"),
    ("tests/fixtures/file1.json", "tests/fixtures/file2.json", 'stylish',
     "tests/fixtures/expected_result_simple.txt"),
    ("tests/fixtures/file3.json", "tests/fixtures/file4.json", 'stylish',
     "tests/fixtures/expected_result_stylish.txt"),
    ("tests/fixtures/file1.yml", "tests/fixtures/file2.yml", 'stylish',
     "tests/fixtures/expected_result_stylish.txt"),
    ("tests/fixtures/file1.yml", "tests/fixtures/file2.yml", 'plain',
     "tests/fixtures/expected_result_plain.txt"),
    ("tests/fixtures/file1.yml", "tests/fixtures/file4.json", 'stylish',
     "tests/fixtures/expected_result_stylish.txt"),
    ("tests/fixtures/file1.yml", "tests/fixtures/file4.json", 'plain',
     "tests/fixtures/expected_result_plain.txt"),
    ("tests/fixtures/file1.json", "tests/fixtures/file2.json", 'json',
     "tests/fixtures/expected_result_simple.json"),
    ("tests/fixtures/file3.json", "tests/fixtures/file4.json", 'json',
     "tests/fixtures/expected_result.json"),
])
def test_generate_diff(file1, file2, formatter, expected):
    diff = generate_diff(file1, file2, formatter)
    expected_result = read_file(expected)
    assert diff == expected_result


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()
