import pytest
from gendiff import generate_diff

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()

@pytest.mark.parametrize("file1, file2, expected", [
    ("tests/fixtures/file1.json", "tests/fixtures/file2.json", "tests/fixtures/expected_result.txt")
])
def test_generate_diff(file1, file2, expected):
    result = generate_diff(file1, file2)
    expected_result = read_file(expected)
    assert result == expected_result
