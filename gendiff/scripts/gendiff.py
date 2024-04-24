import argparse
from gendiff.scripts.generate_diff import generate_diff, format_diff
from gendiff.scripts.parser import read_data


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='first config file')
    parser.add_argument('second_file', help='second config file')
    parser.add_argument('-f', '--format', help='set format of output',
                        default='plain', choices=['plain', 'json'])
    args = parser.parse_args()
    data1 = read_data(args.first_file)
    data2 = read_data(args.second_file)
    diff = generate_diff(data1, data2)
    formatted_diff = '{\n' + format_diff(diff) + '\n}'
    print(formatted_diff)


if __name__ == '__main__':
    main()
