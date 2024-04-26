### Hexlet tests and linter status:
[![Actions Status](https://github.com/Cur1yB/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Cur1yB/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/fabc3436947b7dffb5b5/maintainability)](https://codeclimate.com/github/Cur1yB/python-project-50/maintainability)

# Gendiff: Configuration Files Comparison Tool

## Description

Gendiff is a command line utility for comparing two configuration files. The tool analyzes the files and displays the differences in a human-readable format. It supports JSON and YAML file formats.

## Installation

To install, clone the repository and install using `poetry`:

```sh
git clone https://github.com/Cur1yB/python-project-50
cd gendiff
poetry install
```

## Usage

To display usage information:

```sh
poetry run gendiff -h
```

Example of comparing two files:

```sh
poetry run gendiff filepath1.json filepath2.json
```

The output will appear in the following format:

```json
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

## Command Line Options

- `-h, --help` — display this help message and exit.
- `-f FORMAT, --format FORMAT` — set the output format (supported formats: `plain`, `json`, `stylish`).

## Output Formats

### Stylish

The default format. Shows changes in a tree structure.

### Plain

A flat text format, convenient for human reading:

```sh
Property 'common.follow' was added with value: false
```

### JSON

Outputs the changes in JSON format, convenient for machine processing.

## Development

### Tests

To run tests, use the following command:

```sh
poetry run pytest
```

### Linter

To check the code with the linter, execute:

```sh
make lint
```

## CI/CD

The project uses GitHub Actions for automated testing and linting. You can see the status of the last commit at the top of this README.

[![asciicast](https://asciinema.org/a/ITRxadyv0Y03h1U56YvnKSddN)](https://asciinema.org/a/ITRxadyv0Y03h1U56YvnKSddN?autoplay=1)
