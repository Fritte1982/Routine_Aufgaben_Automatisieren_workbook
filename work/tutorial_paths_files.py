from pathlib import Path
import chardet
from pprint import pprint
import shelve

myFiles = ["account.txt", "detail.csv", "invite.docx"]

for file in myFiles:
    sweigart_path = Path(r"c:\Users\asweigert")
    print(sweigart_path / file)

print(Path.cwd())
Path()

working_dir = Path.cwd()

size = 0
for obj in working_dir.parent.rglob("*"):
    if obj.is_file():
        size += obj.stat().st_size
size_in_mb =size/ 1_000_000
print(size)
print(f"{size_in_mb:.2f} MB")

outputpath = Path.cwd().parent / "output"
if Path.is_dir(outputpath):
    print(f"{outputpath} exists")
testxt_path = outputpath / "hello.txt"
if Path.is_file(testxt_path):
    print(f"{testxt_path.name} exists")
helloFile = open(testxt_path, "rb")
hello_content = helloFile.read()
encoding = chardet.detect(hello_content)
print(f"Vermutetes Encoding: {encoding['encoding']}")

# Dekodiere mit dem vermuteten Encoding
hello_content_str = hello_content.decode(encoding['encoding'])
print(hello_content_str)

sonnet_path = outputpath / "sonnet29.txt"
sonnet_file = open(sonnet_path, "r", encoding="utf-8")
pprint(sonnet_file.read())

shelve_file_path = outputpath / "shelvedata"
shelve_file = shelve.open(shelve_file_path)
cats = ["Zophie", "Poka", "Simon"]
shelve_file["cats"] = cats
shelve_file.close()

shelvefile_open = shelve.open(shelve_file_path)
print(shelvefile_open["cats"])
shelvefile_open.close()