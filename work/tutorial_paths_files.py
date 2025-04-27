from pathlib import Path

myFiles = ["account.txt", "detail.csv", "invite.docx"]

for file in myFiles:
    sweigart_path = Path(r"c:\Users\asweigert")
    print(sweigart_path / file)

print(Path.cwd())
Path()