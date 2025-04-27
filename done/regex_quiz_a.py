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

# Todo Schreiben Sie eine Funktion, die einen String annimmt und das Gleiche macht wie die Stringmethode strip().
#  Wird außer dem String kein anderes Argument übergeben, sollen alle Weißraumzeichen vom Anfang und Ende des Strings entfernt
#  werden. Anderenfalls wird das im zweiten Argument übergebene Zeichen vom Anfang und Ende des Strings entfernt
testtxt = " strip "
original_regex = r"^(\s*)\b(.+)\b(\s*)$"
def regex_strip(text:str, char:str="")->str:
    start_regex = r"^(\s*)\b"
    middle_regex = r"(.+)"
    end_regex = r"\b(\s*)$"
    gesamt_regex = start_regex + middle_regex + end_regex
    subst =r"\2"
    if char:
        subst =f"{char}{subst}{char}"
        result = re.sub(gesamt_regex, subst, text)
    else:
        result = re.sub(gesamt_regex, subst, text)
    return result
print(regex_strip(testtxt,"+"))
