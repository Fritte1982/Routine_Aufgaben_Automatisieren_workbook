import webbrowser, sys, pyperclip
# webbrowser.open("http://inventwithpython.com")

if len(sys.argv) > 1: 
    # Ruft die Adresse von der Befehlszeile ab 
    address = ' '.join(sys.argv[1:]) 
else: 
    # Ruft die Adresse aus der Zwischenablage ab 
    address = pyperclip.paste() 

webbrowser.open('https://www.google.com/maps/place/' + address)
