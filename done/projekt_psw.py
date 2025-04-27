#! python3 

#  projekt_psw.py  - Ein unsicherer Passwortsafe. 
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6', 
            'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt', 
            'luggage': '12345'}

import sys, pyperclip 

if len (sys.argv) < 2 :
    print("Benutzen Sie: python projekt_psw.py [account]  - copy account password")
    sys.exit()

account = sys.argv[1]   # das erste Befehlzeilenargument ist der Kontoname

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Passwort für " + account + " ist in die Zwischenablage kopiert")
else:
    print("Da ist kein Konto namens " + account )