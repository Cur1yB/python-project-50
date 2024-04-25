import argparse
from gendiff.scripts.find_diff import find_diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json_formatter import json_formatter
from gendiff.scripts.parser import parse


def generate_diff(data1, data2, formatter=stylish):
    diff = find_diff(data1, data2)
    diff = formatter(diff)
    return diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='first config file')
    parser.add_argument('second_file', help='second config file')
    parser.add_argument('-f', '--format', help='set format of output',
                        default='stylish', choices=['stylish', 'plain', 'json'])
    args = parser.parse_args()
    data1 = parse(args.first_file)
    data2 = parse(args.second_file)
    if args.format == 'stylish':
        formatter = stylish
    elif args.format == 'json':
        formatter = json_formatter
    else:
        formatter = plain
    diff = generate_diff(data1, data2, formatter)
    print(diff)


if __name__ == '__main__':
    main()
