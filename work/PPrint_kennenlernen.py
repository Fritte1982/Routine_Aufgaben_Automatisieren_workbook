import pprint
from settings import paths_attributes as paths

CAT_FILE_PATH = paths.OUTPUT_FOLDER / "myCats.py"

cats = [{"name": "Zophie", "desc": "chubby"},
        {"name": "Pooka", "desc": "fluffy"}]
pprint.pprint(pprint.pformat(cats))

with open(CAT_FILE_PATH, "w") as f:
        f.write("cats = " + pprint.pformat(cats) + "\n")