import os, zipfile
import send2trash
from settings import paths_attributes

OUTPUT_FOLDER = paths_attributes.OUTPUT_FOLDER
SAMPLES_FOLDER = paths_attributes.SAMPLES_FOLDER
delicious_folder = SAMPLES_FOLDER / "delicious"


bacon_path = OUTPUT_FOLDER / "bacon.txt"
example_zip = paths_attributes.PROJECT_STUFF / "example.zip"

#
# with open(bacon_path, "w") as f:
#     f.write("Bacon is not vegetable. ")
#
# send2trash.send2trash(bacon_path) # Kommt mit pathlib klar, und verschiebt in den Papierkorb statt ganz zu löschen


for foldername, subfolders, filnames in os.walk(delicious_folder):
    # .walk() -> dirpath: str, dirnames: str, filenames: str
    print("the current folder is", foldername)

    for subfolder in subfolders:
        print("SUBFOlDER OF "+ foldername + ": " +  subfolder)
    for filname in filnames:
        print("FILNAME INSIDE "+ foldername + ": " + filname)
    print(" ")


example_zip_obj = zipfile.ZipFile(example_zip, "r")
print (example_zip_obj.namelist())
spam_info = example_zip_obj.getinfo("spam.txt")
print (spam_info.file_size)
print (spam_info.compress_size)
print ('Compressed file is %sx smaller!' % (round(spam_info.file_size / spam_info .compress_size, 2)))

example_zip_obj.extractall(OUTPUT_FOLDER / "example_unzipped")
example_zip_obj.extract("spam.txt", OUTPUT_FOLDER / "one_file_unzipped")

example_zip_obj.close()

os.mkdir(OUTPUT_FOLDER / "zipped")
file_path = OUTPUT_FOLDER / "one_file_unzipped" / "spam.txt"
new_zip = zipfile.ZipFile(OUTPUT_FOLDER / "zipped"/ "spam_zipped.zip", "w")
new_zip.write(file_path, compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()