while True:
    adjektive = input("Eine Adjektive, bitte: ")
    nomen = input("Eine Hauptworte, bitte: ")
    verb = input("Ein Werb, bitte: ")
    
    satz= f"Ein {adjektive} Panda, ging zum {nomen} und tat {verb}."
    print(satz)
    with open('lückentext.txt', "a", encoding="UTF-8") as txt:
        txt.write(satz)
    quite= input("Q/q für beenden: ")
    if quite.lower() == 'q':
        break   
    
with open('lückentext.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        print(line, end = '')
    