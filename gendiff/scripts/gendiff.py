import argparse
from .generate_diff import generate_diff


def main():
    # Создаем парсер и указываем описание программы
    parser = argparse.ArgumentParser(description='Compares two configuration'
                                     + ' files and shows a difference.')
    # Добавляем аргументы для первого и второго файла
    parser.add_argument('first_file', help='first config file')
    parser.add_argument('second_file', help='second config file')
    parser.add_argument('-f', '--format', help='set format of output',
                        default='plain', choices=['plain', 'json'])
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
