from pathlib import Path


myFiles = ['accounts.txt', 'details.csv', 'invite.docx']

P = Path("c:/Users/richard")

for file in myFiles:
    komplett_pfad = P /file
    print(komplett_pfad)

path = Path("../").resolve()
print(path) 

print(Path.cwd())

pfad_ditc_txt = Path(r"F:\Backup-23-01-25-a\D-backup-2023-01-25\desk-ab-21\office-training\Python-ordner-a\Al_Sweigert_Ebooks\Routine_Automatisieren\Onlinematerial_2nd\automate_online-materials\dictionary.txt")

dict_txt = open(pfad_ditc_txt, "r")

print(dict_txt.readlines())