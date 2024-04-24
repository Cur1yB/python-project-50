import pytest
from gendiff.scripts.generate_diff import generate_diff, format_diff
from gendiff.scripts.parser import read_data

@pytest.mark.parametrize("file1, file2, expected", [
    ("tests/fixtures/file3.json", "tests/fixtures/file4.json", "tests/fixtures/expected_result.txt"),
    ("tests/fixtures/file1.json", "tests/fixtures/file2.json", "tests/fixtures/expected_result_simple.txt"),
    ("tests/fixtures/file1.yml", "tests/fixtures/file2.yml", "tests/fixtures/expected_result.txt")
])

def test_generate_diff(file1, file2, expected):
    file1_data = read_data(file1)
    file2_data = read_data(file2)
    diff = generate_diff(file1_data, file2_data)
    
    formatted_diff = '{\n' + format_diff(diff) + '\n}'
    #formatted_diff = format_diff(diff)
    expected_result = read_file(expected)
    print("Formatted Diff:\n", formatted_diff)
    write_file(formatted_diff, "tests/output/actual_result.txt")
    print("Expected Result:\n", expected_result)
    write_file(expected_result, "tests/output/expected_result_in_tests.txt")
    assert formatted_diff == expected_result

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()

def write_file(content, file_name):
    with open(file_name, 'w') as file:
        file.write(content)