import shelve
from pathlib import Path

shelfFile =  shelve.open("mydata_test")
cats = ["Zophie", "Pooka", "Simon"]
shelfFile["cats"] = cats
shelfFile.close()

shelfFile =shelve.open("mydata_test")
print(shelfFile["cats"])
shelfFile.close()
