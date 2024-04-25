def plain(diff):
    lines = plain_formatter(diff)
    result = '\n'.join(lines)
    return result


def plain_formatter(diff, path=""):
    lines = []
    for key, (status, value) in diff.items():
        full_key = create_full_key(path, key)
        if status == "nested":
            lines.extend(plain_formatter(value, full_key))
        elif status == "added":
            lines.append(format_added_property(value, full_key))
        elif status == "removed":
            lines.append(f"Property '{full_key}' was removed")
        elif status == "changed":
            lines.append(format_changed_property(value, full_key))
        elif status == "unchanged":
            continue
    return lines


def create_full_key(path, key):
    if path == "":
        full_key = f"{key}"
    else:
        full_key = f"{path}.{key}"
    return full_key


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, str):
        return f"'{value}'"
    if value is None:
        return "null"
    return str(value).lower()


def format_added_property(value, full_key):
    value = format_value(value)
    if isinstance(value, dict):
        value_description = "[complex value]"
    elif isinstance(value, str):
        value_description = f"{value}"
    else:
        value_description = str(value).lower()
    message = (
        f"Property '{full_key}' was added "
        + f"with value: {value_description}"
    )
    return message


def format_changed_property(value, full_key):
    old, new = value
    old, new = format_value(old), format_value(new)
    if isinstance(old, dict):
        old_value = "[complex value]"
    elif isinstance(old, str):
        old_value = f"{old}"
    else:
        old_value = str(old).lower()
    if isinstance(new, dict):
        new_value = "[complex value]"
    elif isinstance(new, str):
        new_value = f"{new}"
    else:
        new_value = str(new).lower()
    message = (
        f"Property '{full_key}' was updated. "
        + f"From {old_value} to {new_value}"
    )
    return message
