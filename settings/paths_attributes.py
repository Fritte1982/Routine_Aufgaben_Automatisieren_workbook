from pathlib import Path

SETTINGS_FOLDER = Path(__file__).parent
PROJECT_FOLDER = SETTINGS_FOLDER.parent
SOURCES_FOLDER = PROJECT_FOLDER / "sources"
OUTPUT_FOLDER = PROJECT_FOLDER / "output"
SAMPLES_FOLDER = PROJECT_FOLDER / "samples"
PROJECT_STUFF  = PROJECT_FOLDER / "Onlinematerial_2nd" / "automate_online-materials"
AMERICAN_DATE_FOLDER = SOURCES_FOLDER / "american_date_formate"
LUECKEN_FILES_FOLDER = SOURCES_FOLDER / "lücken_files"

def main():
    if LUECKEN_FILES_FOLDER.exists() and AMERICAN_DATE_FOLDER.exists():
        print("folders exists")

if __name__ == '__main__':
    main()