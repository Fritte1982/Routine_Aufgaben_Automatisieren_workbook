from pathlib import Path

SETTINGS_FOLDER = Path(__file__).parent
PROJECT_FOLDER = SETTINGS_FOLDER.parent
SOURCES_FOLDER = PROJECT_FOLDER / "sources"
OUTPUT_FOLDER = PROJECT_FOLDER / "output"


def main():
    if OUTPUT_FOLDER.exists() and SOURCES_FOLDER.exists():
        print("Settings folder exists")

if __name__ == '__main__':
    main()