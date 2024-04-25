import pytest
from gendiff.scripts.gendiff import generate_diff
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from gendiff.scripts.parser import parse
from gendiff.formatters.json_formatter import json_formatter
from gendiff import generate_diff

@pytest.mark.parametrize("file1, file2, formatter, expected", [
    ("tests/fixtures/file3.json", "tests/fixtures/file4.json", plain, "tests/fixtures/expected_result_plain.txt"),
    ("tests/fixtures/file1.json", "tests/fixtures/file2.json", stylish, "tests/fixtures/expected_result_simple.txt"),
    ("tests/fixtures/file3.json", "tests/fixtures/file4.json", stylish, "tests/fixtures/expected_result_stylish.txt"), 
    ("tests/fixtures/file1.yml", "tests/fixtures/file2.yml", stylish, "tests/fixtures/expected_result_stylish.txt"),
    ("tests/fixtures/file1.yml", "tests/fixtures/file2.yml", plain, "tests/fixtures/expected_result_plain.txt"),
    ("tests/fixtures/file1.yml", "tests/fixtures/file4.json", stylish, "tests/fixtures/expected_result_stylish.txt"),
    ("tests/fixtures/file1.yml", "tests/fixtures/file4.json", plain, "tests/fixtures/expected_result_plain.txt"),
    ("tests/fixtures/file1.json", "tests/fixtures/file2.json", json_formatter, "tests/fixtures/expected_result_simple.json"),
    ("tests/fixtures/file3.json", "tests/fixtures/file4.json", json_formatter, "tests/fixtures/expected_result.json"),
])

def test_generate_diff(file1, file2, formatter, expected):
    file1_data = parse(file1)
    file2_data = parse(file2)
    diff = generate_diff(file1_data, file2_data, formatter)
    expected_result = read_file(expected)
    print("Formatted Diff:\n", diff)
    write_file(diff, "tests/output/actual_result.txt")
    print("Expected Result:\n", expected_result)
    write_file(expected_result, "tests/output/expected_result_in_tests.txt")
    assert diff == expected_result

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()

def write_file(content, file_name):
    with open(file_name, 'w') as file:
        file.write(content)