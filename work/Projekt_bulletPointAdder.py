#! python3
# projekt_bulletPointAdder.py- fügt Wikipedia-Aufzählungszeichen zu Beginn jeder
# Zeile des Textes in der Zwischenablage hinzu.
import pyperclip

text = pyperclip.paste()

print(text)

text_liste = text.split('\n')
print(text_liste)
text_liste.remove("")
#text_liste = text_liste.remove("")
for i, v in enumerate(text_liste):
    str(text_liste[i]).strip('\r')
    text_liste[i] = "* " +text_liste[i]
    print (text_liste[i])
text = '\n'.join(text_liste)

pyperclip.copy(text)