from settings import paths_attributes
import re

LUECKEN_FILES = paths_attributes.LUECKEN_FILES_FOLDER

pattern = r"\d{3}"
regex = re.compile(pattern)

min_int =0
max_int = 0
count_int = 0
for file in LUECKEN_FILES.iterdir():
    match = re.search(pattern, file.name)
    if match:
        numeric_string = match.group()
        integer =int(numeric_string)
        count_int += 1
print(count_int)
i =0
new_names = []
for file in LUECKEN_FILES.iterdir():
    # for i in range(count_int):
    match = re.search(pattern, file.name)
    if match:
        i = i + 1
        range_number = i
        new_numeric_chars = f"00{range_number}"
        new_filename = re.sub(pattern, new_numeric_chars, file.name)
        new_names.append(new_filename)

        if file.name not in new_names:
            new_path = file.parent / new_filename
            print(new_path)
        else:
            continue
