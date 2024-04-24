import json
import yaml
import os


def read_data(file_path):
    extension = os.path.splitext(file_path)[1].lower()
    parser = {
        '.json': json.load,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load
    }

    if extension not in parser:
        raise ValueError(f"Unsupported file format: {extension}")

    with open(file_path) as file:
        return parser[extension](file)


def parse(content, file_extension):
    if file_extension in ('.json',):
        return json.loads(content)
    elif file_extension in ('.yaml', '.yml',):
        return yaml.safe_load(content)
    else:
        raise ValueError(f"Unsupported file format: {file_extension}")
