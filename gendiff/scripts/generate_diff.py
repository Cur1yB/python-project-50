import json


def generate_diff(file_path1, file_path2):
    with open(file_path1) as file1, open(file_path2) as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

    diff = {}
    all_keys = sorted(set(data1.keys()).union(data2.keys()))

    for key in all_keys:
        if key in data1 and key not in data2:
            diff[key] = f"- {key}: {data1[key]}"
        elif key not in data1 and key in data2:
            diff[key] = f"+ {key}: {data2[key]}"
        elif data1[key] != data2[key]:
            diff[key] = [f"- {key}: {data1[key]}", f"+ {key}: {data2[key]}"]
        else:
            diff[key] = f"  {key}: {data1[key]}"

    result = ["{"] + [f"  {v}" if isinstance(v, str) else f"  {v[0]}\n  {v[1]}"
                      for v in diff.values()] + ["}"]
    return "\n".join(result)
