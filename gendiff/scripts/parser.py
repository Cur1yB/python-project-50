import json
import yaml
import os


def parse(file_path):
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
