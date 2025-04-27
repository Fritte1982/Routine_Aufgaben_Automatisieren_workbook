import zipfile
from pathlib import Path
import os 
import pathlib
zipdatei = (r"F:\Backup-23-01-25-a\D-backup-2023-01-25\desk-ab-21\office-training"
r"\Python-ordner-a\python-scripts_vs-code\sonstige_projekte\python_Ai_Sweigert"
r"\Routine_Aufgaben_Automatisieren\neu.zip")



zipdatei = pathlib.PureWindowsPath(zipdatei)


#zipdatei = Path(zipdatei)

exampleZip = zipfile.ZipFile(zipdatei,"r")


print(exampleZip.namelist())