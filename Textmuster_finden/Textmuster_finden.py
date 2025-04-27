import re


telephone_in_string = r"""drei Ziffern, ein 
Bindestrich, drei Ziffern, ein weiterer Bindestrich und schließlich vier Ziffern, 
beispielsweise 415-555-4242."""

tele_number_alone = r"415-555-4242"

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

def isPhoneNumber(txt: str)-> bool:
    if len(txt) != 12:
        return False
    for i in range(0, 3):
        if not txt[i].isdecimal():
            return False
    if txt[3] != '-':
        return False    
    for i in range(4, 7):
        if not txt[i].isdecimal():
            return False
    if txt[7] != '-':
        return False   
    for i in range(8, 12):
        if not txt[i].isdecimal():
            return False
    return True

def phoneNumber_in_txt(string: str)->None:
    for i in range(len(string)):
        sub12string= string[i:i+12]
        if isPhoneNumber(sub12string):
            print("Telefonnummer gefunden: " + sub12string)
    print("Text durchsuchen fertig.")

phoneNumber_in_txt(telephone_in_string)
phoneNumber_in_txt(message)
print(isPhoneNumber(tele_number_alone))
mynumber_txt = "My number is 415-555-4242."

phoneNumRegex = re.compile(r"\d{3}-\d{3}-\d{4}")
mo = phoneNumRegex.search("My number is 415-555-4242.")
print('Phone number found: ' + mo.group())

# Guppierung durch Klammern routine-automatisieren Seite 197
phoneNumRegex = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
mo =phoneNumRegex.search(mynumber_txt)
print(mo.group(1))
print(mo.group(0))
print(mo.group())
print(mo.groups())

# Mithilfe der Pipe nach Übereinstimmungen mit mehreren Gruppen suchen , seite 199

teststring = "Batman and Tina Fey"
teststring2 = "Tina Fey and Batman"
heroRegex = re.compile(r"Batman|Tina Fey")
mo1= heroRegex.search(teststring)
print(mo1.group())
mo2= heroRegex.search(teststring2)
print(mo2.group())

batmobile_string = "Batmobile lost a Wheel"
batRegex = re.compile(r"Bat(man|mobile|copter|bat)")
mo = batRegex.search(batmobile_string)
print(mo.group())

# Optionale Übereinstimmung mit dem Fragezeichen, Seite 200
batstring = 'The Adventures of Batman'
womanstring = "The Adventures of Batwoman"
batRegex = re.compile(r"Bat(wo)?man")
mo1 = batRegex.search(batstring)
print(mo1.group())

mo2 = batRegex.search(womanstring)
print(mo2.group())

# Mit dem Sternchen nach null oder mehr Übereinstimmungen suchen, Seite 200
wowomanstring ='The Adventures of Batwowowowoman'
batRegex = re.compile(r"Bat(wo)*man")
mo = batRegex.search(womanstring)
print(mo.group())

mo2 = batRegex.search(wowomanstring)
print(mo2.group())

# Mit dem Pluszeichen nach einer oder mehr Übereinstimmungen suchen, Seite 201
batRegex = re.compile(r"Bat(wo)+man")
mo1= batRegex.search(womanstring)
print(mo1.group())
mo2= batRegex.search(wowomanstring)
print(mo2.group())
mo3 = batRegex.search(batstring)
print(mo3 == None) 

# Gieriger und nicht gieriger Mustervergleich, Seite 203
#Reguläre Ausdrücke sind in Python standardmäßig gierig (»greedy«), was 
#bedeutet, dass in mehrdeutigen Situationen der längstmögliche String gefunden wird.

#Um die nicht gierige Version der geschweiften Klammern zu verwenden, die 
#den kürzestmöglichen String zurückgibt, müssen Sie hinter die Klammern ein Fragezeichen stellen.

haha_string = "HaHaHaHaHa"
nogreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo = nogreedyHaRegex.search(haha_string)
print(mo.group())

# Die Methode findall(), Seite 203
#Dagegen gibt findall() kein Match-Objekt zurück, sondern eine Liste der Strings aller Übereinstimmungen
#oder eine liste der Gruppen als Tupel.

phone_string = 'Cell: 415-555-9999 Work: 212-555-0000'
phoneNumRegex = re.compile(r"\d{3}-\d{3}-\d{4}") # ohne Gruppe, findall gibt liste mit strings zurück
liste_strings =phoneNumRegex.findall(phone_string)
print(liste_strings)

phone_string = 'Cell: 415-555-9999 Work: 212-555-0000'
phoneNumRegex = re.compile(r"(\d{3})-(\d{3})-(\d{4})") # mit Gruppen, findall gibt liste mit Tupeln zurück
liste_tupel =phoneNumRegex.findall(phone_string)
print(liste_tupel)
#Wird die Methode findall() auf reguläre Ausdrücke mit Gruppen angewendet, z. B. (\d\d\d)-(\d\d\d)-(\d\d\d\d), so gibt sie eine Liste von Tupeln aus 
#Strings zurück (mit je einem String für jede Gruppe), z. B. [('415', '555', '1122'), ('212', '555', '0000')].

# Übersicht über Regex-Symbole, Seite 209

