import re, pyperclip

phonRegex = re.compile(r"""(
                        (\d{3}|\(\d{3}\))?      # Bereichsvorwahl
                        (\s|-|\.)?              # trennzeichen
                        (\d{3})                   # ersten 3 Stellen
                        (\s|-|\.)               # Trennzeichen
                        (\d{4})                   # Letzten 4 Stellen
                        (\s*(ext|x|ext.)\s*(\d{2.5}))?    # Durchwahl
                        )""",re.VERBOSE)

emailRegex = re.compile(r"""(
                            [a-zA-Z0-9._%+-]+    # Benutzername
                            @                    # @-Symbole
                            [a-zA-Z0-9.-]+       # Domänenname
                            (\.[a-zA-Z]{2,4})    # Punkt + iregendetwas 
                            )""", re.VERBOSE)
# findet Übereinstimmungen im Text ind er Zwischenablage-
text = str(pyperclip.paste())
matches = []
for gruppe in phonRegex.findall(text):
    phoneNum = '-'.join([gruppe[1], gruppe[3], gruppe[5]])
    if gruppe[8] != "":
        phoneNum = phoneNum + " x" + gruppe [8]
    matches.append(phoneNum)
    
for gruppe in emailRegex.findall(text):
    matches.append(gruppe[0]) 
print(matches)

# kopiert die Ergebnisse in die Zwischenablage
if len (matches) > 9:
    pyperclip.copy("\n".join(matches))
    print("In die Zwischenablage kopiert: ")
    print("\n".join(matches))
else:
    print("Keine Email oder Telefonnummer gefunden. ")