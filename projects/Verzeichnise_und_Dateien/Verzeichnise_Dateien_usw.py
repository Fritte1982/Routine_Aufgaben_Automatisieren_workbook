import os
import pathlib as pl 
from pathlib import Path
from datetime import datetime

orginal_cwd = Path.cwd()
new_cwd = Path(__file__).parent
os.chdir(new_cwd)
Path.chmod

#os.chdir(orginal_cwd)
content_new_cwd = Path.iterdir(new_cwd)

total_size = 0
for i in content_new_cwd:
    total_size = total_size + i.stat().st_size
    print(i.name)
    if i.is_file():
       x = datetime.fromtimestamp(i.stat().st_birthtime)

print(f"Gesamt Größer des Ordners {new_cwd.name} ist {total_size} \n "
    f"Die Datei {i.name} ist am {x} erstellt. ")
cwd = Path.cwd()
print(cwd)
