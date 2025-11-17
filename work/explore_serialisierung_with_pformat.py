import pprint
from settings import paths_attributes
OUTPUT_FOLDER = paths_attributes.OUTPUT_FOLDER
OUTPUT_FILE_PATH = OUTPUT_FOLDER / "cats_serialisierung.py"

cats = [
    {'name': 'Zophie', 'desc': 'chubby'},
    {'name': 'Pooka', 'desc': 'fluffy'}
]

filObj = open(OUTPUT_FILE_PATH, 'w')
filObj.write('cats = ' + pprint.pformat(cats) + '\n')
filObj.close()
filObj.close()
