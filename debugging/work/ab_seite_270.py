import traceback
from pprint import pprint

PATH_ERROR_FILE: str = (
    r"F:\Backup-23-01-25-a\D-backup-2023-01-25\desk-ab-21\office-training\Python-ordner-a"+
    r"\python-scripts_vs-code\sonstige_projekte\python_Ai_Sweigert"+
    r"\Routine_Aufgaben_Automatisieren\debugging\output\errorInfo.txt"
    )


def boxPrint(symbol, width, height):
    if len(symbol) !=1:
        raise Exception("Die Variable 'symbole' daf nur ein Zeichen sein. ")
    if width <= 2:
        raise Exception("'width' muss größer als 2 sein.")
    if height <= 2:
        raise Exception("'height' muss gößer als 2 sein.")
    print(symbol*width)
    for i in range(height - 2): 
        print(symbol + (' ' * (width - 2)) + symbol) 
    print(symbol * width)
        
for sym, w, h in (("*", 4, 4), ("0", 20, 5),("x",1, 3), ('ZZ',3,3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print("Eine Ausnahme ist pasiert: " + str(err))
        
try:
    raise Exception("Das ist eine Fehlermeldung die in die Datei gespeicher wird.")
except:
    with open(PATH_ERROR_FILE, "w") as errFile:
        errFile.write(traceback.format_exc())
        print("Der Traceback wurde in 'errorInfo.txt' geschrieben. ")


podBayDoorStatus = "open"
assert podBayDoorStatus == 'open', "Das Tor braucht den string 'open' "
podBayDoorStatus = "Entschuldigung, Dave. Ich fürchte, das kann ich nicht tun."
# assert podBayDoorStatus == 'open', "Das Tor braucht den string 'open' "

market_2nd = {
    "ns": "green",
    "ew": "red"
    }
mission_16th = {
    "ns": "red",
    "ew": "green"
    }

def swich_lights(stoplights: dict):
    for k, v in stoplights.items():
        assert "red" in stoplights.values(), "es muss eine Ampel der Wert 'red'  haben" + str(stoplights)
        if v == "green":
            stoplights[k] = 'yellow'
        elif v == 'yellow':
            stoplights[k] = "red"
        elif v == 'red':
            stoplights[k] = 'green'
        assert "red" in stoplights.values(), "es muss eine Ampel der Wert 'red'  haben " + str(stoplights)

swich_lights(market_2nd)  
pprint(market_2nd)