"""Das Programm soll folgende Aufgaben erledigen:"""
# TODO: Die Befehlszeilenargumente untersuchen
# TODO: Bei dem Argument save den Inhalt der Schlüsselablage unter dem angegebenen Schlüsselwort speichern
# TODO: Bei dem Argument list alle Schlüsselwörter in die Zwischenablage kopieren
# TODO: Anderenfalls den unter dem übergebenen Schlüsselwort gespeicherten Text in  die Zwischenablage übertragen

from settings import paths_attributes
import shelve
import sys
import logging
import pyperclip

logger = logging.getLogger(__name__)
logger.propagate = False
logger.handlers.clear()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formater = logging.Formatter('%(name)s - %(levelname)s -|<- \n ->%(message)s')
handler.setFormatter(formater)
logger.addHandler(handler)

data_file_path = paths_attributes.OUTPUT_FOLDER / "clipboard_shelve"


cli_args = sys.argv


temp_clip = pyperclip.paste()

dummy = "Test"
logger.info(cli_args)
if "save" in cli_args and cli_args[2]:
    with shelve.open(data_file_path) as shelf:
        shelf[cli_args[2]] = temp_clip
    logger.info("Save is in args")
elif "list" in cli_args:
    with shelve.open(data_file_path) as shelf:
        logger.info(list(shelf.keys()))
elif len(cli_args) == 3 and cli_args[1] == "delete" :
    with shelve.open(data_file_path) as shelf:
         del shelf[cli_args[2]]
elif len(cli_args) == 2 and cli_args[1] == "delete" :
    with shelve.open(data_file_path) as shelf:
        for key in shelf.keys():
            del shelf[key]
else:
    with shelve.open(data_file_path) as shelf:
        temp =shelf[cli_args[1]]
    logger.info(temp)
