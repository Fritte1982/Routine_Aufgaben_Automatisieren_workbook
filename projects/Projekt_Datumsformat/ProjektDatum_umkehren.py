import re, os, shutil
from pathlib import Path
from typing import List

Pfad_Dateien = (r"F:\Backup-23-01-25-a\D-backup-2023-01-25\desk-ab-21\office-training\Python-ordner-a"
r"\python-scripts_vs-code\sonstige_projekte\python_Ai_Sweigert"
r"\Routine_Aufgaben_Automatisieren\Projekt_Datumsformat\Dateien")

Pfad_Dateien = Path(Pfad_Dateien)

regex =r"""(.{0,})# Gruppe 1  Text vor dem Datum oder Leerstring
([0-1][0-9]\W)# gruppe 2 Monat, im Orginal mit anschliessenden "-"
([0-3][0-9]\W)# Gruppe 3 Tag, im Original mit anschliessenden  '-'
(\d{4})        # Gruppe 4 Jahr, bleibt so 
(.*)            # Gruppe 5 Tex nach dem Datum einschlisslich Dateiendung
"""
regex =re.compile(regex, re.VERBOSE)

matches: List[re.Match] = []
for dateien in Pfad_Dateien.iterdir():
    if dateien.is_file():
        mo= re.finditer(regex,dateien.name)
        for i in mo:
            matches.append(i)
orginal_namen = []
for i in matches:
    groups =i.groups()
    print("Groups anzahl:", len(groups))
    print()
    print("gruppe 1: ",i.group(1))
    print("gruppe 2: ",i.group(2))
    #print("gruppe 3: ",i.group(3))
    orginal_namen.append(i.group(0))
    
print()
for orignale in Pfad_Dateien.iterdir():
    for i in matches:
        groups = i.groups()
        vorheriger_text = i.group(1)
        monat = i.group(2)
        tag = i.group(3)
        jahr = i.group(4)
        text_nach_dem_datum = i.group(5)

        neues_datum = f"{tag[:-1]}-{monat[:-1]}-{jahr}"
        neuer_dateiname = f"{vorheriger_text}{neues_datum}{text_nach_dem_datum}"

        # Neuer Dateipfad
        neuer_pfad = Pfad_Dateien / neuer_dateiname

        # Überprüfe, ob der neue Dateipfad bereits existiert
        if neuer_pfad.exists():
            print(f"Datei {neuer_dateiname} existiert bereits.")
        else:
            # Versuche, die Datei umzubenennen, wenn der neue Dateipfad noch nicht existiert
            orignale = Pfad_Dateien / i.group(0)
            orignale.rename(neuer_pfad)
            print(f"Datei umbenannt: {orignale.name} -> {neuer_dateiname}")
