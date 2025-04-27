import os
from pathlib import Path
import pprint
verzeichnis = r"F:\Backup-23-01-25-a\D-backup-2023-01-25\desk-ab-21\office-training\Python-ordner-a\python-scripts_vs-code"
verzeichnis= Path(verzeichnis)
for ordner , unterordner, dateien_ in os.walk(verzeichnis):
    #print("Der aktulle Ordner ist", ordner)
    pass
    for u_ordner in unterordner:
        #print ("Der Unterordner von" + ordner + " ist " + u_ordner )
        pass
    for datei in dateien_:
        if datei.endswith(".zip"):
            print("Datei in " + ordner + " ist " + datei)
