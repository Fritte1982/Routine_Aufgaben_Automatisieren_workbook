# ! Pyhon3
# übung_datumsformat.py ändert amerikanische MM-DD-YYY-Datumsangaben in 
# Dateinamen in europäische DD-MM-YYYY-Datumsangaben.
# Routine-Aufgaben-Automatisieren Seite 260

import shutil, pathlib, re
from settings import paths_attributes

source_date_folder = paths_attributes.AMERICAN_DATE_FOLDER

regex_source_files = re.compile(r"(?P<am_file>(?P<am_date>"
                                r"(?P<am_month>[01]?[0-9]?){1}-"
                                r"(?P<am_day>[0-3]?[0-9]?){1}-"
                                r"(?P<am_year>\d{4}){1})"
                                r"(?P<am_name>.*))", re.VERBOSE)

for path in source_date_folder.iterdir():
    filename = path.name
    new_filename = regex_source_files.sub(r"\g<am_day>-\g<am_month>-\g<am_year>\g<am_name>", str(filename))
    print(new_filename)
    dirPath = path.parent
    destPath =  dirPath / new_filename
    if new_filename != filename:
        print(destPath)

