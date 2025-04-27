import traceback 

OUTPUT_PATH =(
    r"F:\Backup-23-01-25-a\D-backup-2023-01-25\desk-ab-21\office-training\Python-ordner-a" + 
    r"\python-scripts_vs-code\sonstige_projekte\python_Ai_Sweigert" + 
    r"\Routine_Aufgaben_Automatisieren\debugging\output"
    )

path_errortxt = OUTPUT_PATH + r"\errorInfo.txt"


def boxPrint(symbol, width,height):
    if len(symbol) !=1:
        raise Exception('Symbol must be a single character string.') 
    if width <=2:
        raise Exception('Width must be greater than 2.') 
    if height <= 2: 
        raise Exception('Height must be greater than 2.')
    print(symbol * width) 
    for i in range(height - 2): 
        print(symbol + (' ' * (width - 2)) + symbol) 
    print(symbol * width) 
    
for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try: 
        boxPrint(sym, w, h) 
    except Exception as err:
        print('An exception happened: ' + str(err))

try:
    raise Exception("This is in Error message")
except:
    errorFile = open(path_errortxt, "w")
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print("The Traceback was written in the File")
    
