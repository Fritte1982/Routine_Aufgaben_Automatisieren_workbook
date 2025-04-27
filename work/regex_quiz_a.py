import  re

# Todo Regex für Passwortstärke mind 8 Zeichen, mind.1 klein und Großbuchstaben, mind 1. Ziffer

testpasswort = "Richard5"

regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
regex = re.compile(regex)

mo = regex.search(testpasswort)
if mo:
    print(f"'{mo.group()}'", "ist ein starkes Passwort")
else:
    print("Das Passwort ist nicht Stark genug")