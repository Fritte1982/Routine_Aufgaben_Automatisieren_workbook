#! <C:\ProgramData\Anaconda3\envs\New_version\python.exe>
#! <C:\Users\richa\AppData\Local\Programs\Python\Python311\python.exe>



import os, sys 
sys.path.append(r"C:\ProgramData\Anaconda3\envs\New_version\Lib\site-packages")
from pathlib import Path
import shelve
import pyperclip # Dritt-Anbieter Package fürs Clpiboard

MCB_PROJEKT_ORDNER = Path(
    r"/projects/projekt_mcb")
os.chdir(MCB_PROJEKT_ORDNER)

print(Path.cwd())

# mcb.pyw - Speichert Text und Lädt ihn in die Zwischenablage
# Nutzung: py.exe mcb.pyw save <Schlüssel> -    Speichert den Inhalt der Zwischenablage
#                                               unter dem Schlüssel
#          py.exe mcb.pyw <Schlüssel> -   lädt den Wert zu dem Schlüssel 
#                                         in die Zwischenablage
#          py.exe mcb.pyw list - Lädt alle Schlüsselwörter in die Zwischenablage

mcbShelve_path = r"/projects/projekt_mcb\mcb"

mcbShelve = shelve.open(mcbShelve_path)

# speichert den Inhalt in die Zwischenablage.
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcbShelve[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == "delete":
    try:
        mcbShelve.pop(sys.argv[2])
    except KeyError:
        print("Schlüssel nicht vorhanden")
elif len(sys.argv) == 2 and sys.argv[1].lower() == "delete":
    mcbShelve.clear()
# listet Schüsselwörter und lädt Inhalte.
elif len(sys.argv) == 2 and sys.argv[1].lower() == "list":
    pyperclip.copy(str(list(mcbShelve.keys())))
elif len(sys.argv) == 2 and sys.argv[1] in mcbShelve:
    pyperclip.copy(mcbShelve[sys.argv[1]])
else:
    pass


mcbShelve.close()