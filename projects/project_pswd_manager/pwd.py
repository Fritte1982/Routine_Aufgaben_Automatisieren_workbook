#! python3
# pw.py - Ein unsicherer Passwortsafe.
import logging
import sys
import pyperclip

logger = logging.getLogger("summary_functions")
logger.propagate = False #<-
logger.handlers.clear() #<-
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout) #
formatter = logging.Formatter("%(message)s")
handler.setFormatter(fmt=formatter)

logger.addHandler(handler)


PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
 'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
 'luggage': '12345'}

if len(sys.argv) < 2:
    print("Usage: python pwd_py [account] - copy account password")
account = sys.argv[1]    # Das erste Befehlszeilenargument ist der Kontoname

logger.info(sys.argv)
if PASSWORDS.get(account):
    pyperclip.copy(PASSWORDS[account])
    print(PASSWORDS[account])
else:
    print("Account does not exist")


