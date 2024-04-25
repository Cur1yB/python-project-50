import argparse
from gendiff.scripts.generate_diff import generate_diff
from gendiff.scripts.stylish import stylish
from gendiff.scripts.plain import plain
from gendiff.scripts.parser import parse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='first config file')
    parser.add_argument('second_file', help='second config file')
    parser.add_argument('-f', '--format', help='set format of output',
                        default='stylish', choices=['stylish', 'plain'])
    args = parser.parse_args()
    data1 = parse(args.first_file)
    data2 = parse(args.second_file)
    if args.format == 'stylish':
        formatter = stylish
    else:
        formatter = plain
    diff = generate_diff(data1, data2, formatter)
    print(diff)


if __name__ == '__main__':
    main()
