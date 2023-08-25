import os

dirpath, directories, files = next(os.walk('.'))

file_dict = {}
for el in files:
    value, key = el.split(".")
    if key not in file_dict:
        file_dict[key] = []
    file_dict[key].append(value)

file_dict = dict(sorted(file_dict.items(), key = lambda kvp: kvp))


for key, value in file_dict.items():
    value.sort()
    result = f".{key}"
    for el in value:
        result += "\n" + f"- - - {el}.{key}"
    print(result)