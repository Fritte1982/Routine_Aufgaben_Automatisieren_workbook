from settings import paths_attributes
import os
import shutil

OUTPUT_TASKS_FILE_MANAGEMENT = paths_attributes.OUTPUT_FOLDER / "chap_file_management_out"
PROJECT_STUFF_FOLDER = paths_attributes.PROJECT_STUFF


def select_copy(source_path, destination_path, praefix=".pdf"):
    if not destination_path.exists():
        os.mkdir(destination_path)

    for item in source_path.iterdir():
        if item.is_file() and str (item.name).endswith(praefix):
            item_dest_path = destination_path / item.name
            print(item_dest_path)
            shutil.copy(str(item), str(item_dest_path))
            print("Copied")

select_copy( PROJECT_STUFF_FOLDER, OUTPUT_TASKS_FILE_MANAGEMENT)




