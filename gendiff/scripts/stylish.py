def stylish(diff):
    result = '{\n' + tree_view(diff) + '\n}'
    return result


def tree_view(diff, depth=1):
    lines = []
    for key, (type, value) in sorted(diff.items()):
        lines = create_formatted_line(lines, key, value, depth, type)
    result = '\n'.join(lines)
    return result


def create_formatted_line(lines, key, value, depth, type):
    prefix = '  '
    if type == 'nested':
        indent = (4 * depth - 2) * ' '
        child_diff = tree_view(value, depth + 1)
        formated_value = f'{{\n{child_diff}\n{indent}  }}'
        lines = add_indent_and_format(depth, lines, prefix, key, formated_value)
    elif type == 'changed':
        lines = changed_data_diff(lines, value, depth, key)
    elif type == 'added':
        prefix = '+ '
        lines = add_indent_and_format(depth, lines, prefix, key, value)
    elif type == 'removed':
        prefix = '- '
        lines = add_indent_and_format(depth, lines, prefix, key, value)
    else:
        lines = add_indent_and_format(depth, lines, prefix, key, value)
    return lines


def add_indent_and_format(depth, lines, prefix, key, value):
    formated_value = format_value(value, depth + 1)
    indent = (4 * depth - 2) * ' '
    lines.append(f"{indent}{prefix}{key}: {formated_value}")
    return lines


def format_value(value, depth):
    if isinstance(value, dict):
        prefix = '  '
        lines = ['{']
        for key, val in value.items():
            formated_value = format_value(val, depth + 1)
            lines = add_indent_and_format(depth, lines,
                                          prefix, key, formated_value)
        indent = ' ' * (4 * (depth - 1))
        lines.append(f"{indent}}}")
        return '\n'.join(lines)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return value
    return str(value)


def changed_data_diff(lines, value, depth, key):
    old, new = value
    old_new_pairs = [('- ', old), ('+ ', new)]
    for prefix, value in old_new_pairs:
        formated_value = format_value(value, depth + 1)
        lines = add_indent_and_format(depth, lines, prefix, key, formated_value)
    return lines
