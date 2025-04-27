import re

psw = "Abcdehi5"

länge_passwort_regex= re.compile(r".{8,}")
großbuchstabe_regex = re.compile(r"[A-Z]")
Kleinbuchstaberegex = re.compile(r"[a-z]")
zifferregex = re.compile(r"[0-9]")

starkes_psw = True
if länge_passwort_regex.search(psw) is None:
    starkes_psw = False
if großbuchstabe_regex.search(psw) is None:
    starkes_psw = False
if Kleinbuchstaberegex.search(psw) is None:
    starkes_psw = False
if zifferregex.search(psw) is None:
    starkes_psw = False

    
print(f"{psw} ist ein Starkes, Passwort, ist {starkes_psw}")

