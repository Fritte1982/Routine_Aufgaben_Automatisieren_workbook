import re

text ='415-555-4242'

print (text)


def isPhoneNumber(string: str)  -> bool:
    if len(string) != 12:
        return False
    for i in range(0,3):
        if not string[i].isdecimal():
            return False
    if string[3] != '-':
            return False
    for i in range(4,7):
        if not  string[i].isdecimal():
            return False
    for i in range(8, 12):
        if not string[i].isdecimal():
            return False
    return True

print(isPhoneNumber(text))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)): 
    chunk = message[i:i+12] 
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk) 
print('Done')

phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)") # die Variable enthält jetzt ein
                                                # Regex-Objekt im Format der Telefonummer.
mo = phoneNumRegex.search('My number is 415-555-4242.') 
print("Telefonnummer gefunden: " + mo.group(2))

phoneNumRegex = re.compile(r"\d{3}-\d{3}-\d{4}")
mo = phoneNumRegex.search('My number is 415-555-4242.') 
print("Telefonnummer gefunden: " + mo.group())