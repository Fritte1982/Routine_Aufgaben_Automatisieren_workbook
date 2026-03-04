import traceback
from settings import paths_attributes

DEBUG_FILE = paths_attributes.DEBUG_OUTPUT_FOLDER / "errorInfo_2.txt"



# def spam():
#     bacon()
#
# def bacon():
#     raise Exception("Eine Fehlermeldung")
# spam()

try:
    raise Exception("Eine Fehlermeldung")
except:
    errorFile =open(DEBUG_FILE,"w")
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print("Traceback write in: {0}".format(DEBUG_FILE))