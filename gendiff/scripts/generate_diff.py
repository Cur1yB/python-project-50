def generate_diff(data1, data2):
    keys = sorted(set(data1.keys()).union(data2.keys()))
    diff = {}

    for key in keys:
        if key in data1 and key not in data2:
            diff[key] = ('removed', data1[key])
        elif key not in data1 and key in data2:
            diff[key] = ('added', data2[key])
        elif data1[key] == data2[key]:
            diff[key] = ('unchanged', data1[key])
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = ('nested', generate_diff(data1[key], data2[key]))
        else:
            diff[key] = ('changed', (data1[key], data2[key]))

    return diff


def format_diff(diff, depth=1):
    lines = []
    indent = (4 * depth - 2) * ' '
    for key, (type, value) in sorted(diff.items()):
        lines = diff_formatter(lines, indent, key, value, depth, type)
    result = '\n'.join(lines)
    return result


def diff_formatter(lines, indent, key, value, depth, type):
    prefix = '  '
    if type == 'nested':
        child_diff = format_diff(value, depth + 1)
        lines.append(
            f"{indent}{prefix}{key}: {{\n{child_diff}\n{indent}  }}"
        )
    elif type == 'changed':
        old, new = value
        lines.append(f"{indent}- {key}: {format_value(old, depth + 1)}")
        lines.append(f"{indent}+ {key}: {format_value(new, depth + 1)}")
    elif type == 'added':
        prefix = '+ '
    elif type == 'removed':
        prefix = '- '
    if type != 'nested' and type != 'changed':
        formatted_value = format_value(value, depth + 1)
        lines.append(f"{indent}{prefix}{key}: {formatted_value}")
    return lines


def format_value(value, depth):
    if isinstance(value, dict):
        indented = (4 * depth - 2) * ' '
        lines = ['{']
        for key, val in value.items():
            lines.append(f"{indented}  {key}: {format_value(val, depth + 1)}")
        lines.append(f"{' ' * (4 * (depth - 1))}}}")
        return '\n'.join(lines)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return value
    return str(value)
