#! python3 
# randomQuizGenerator.py - Erstellt Testfragebogen mit Fragen und Antworten 
# in zufälliger Reihenfolge sowie die zugehörigen Lösungsbogen 
import random, os 
from pathlib import Path

projekt_ordner = Path(r"F:\Backup-23-01-25-a\D-backup-2023-01-25\desk-ab-21\office-training\Python-ordner-a\python-scripts_vs-code\sonstige_projekte\python_Ai_Sweigert\Routine_Aufgaben_Automatisieren\RandomQuiz_projekt")
os.chdir(projekt_ordner)
print(Path.cwd())
# Die abzufragenden Daten. Die Schlüssel sind die Bundesstaaten, die Werte 
# deren Hauptstädte. 
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona':  
'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 
'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 
'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 
'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 
'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 
'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 
'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 
'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville',
'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 
'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'} 

# Erstellt 35 Testfragebogen 
for quizNum in range(35): 
    # erstellt die Dateien für die Fragen und Lösungsbögen
    quizFile = open(f"capitalsquiz{quizNum +1}.txt", "w")
    answerKeyFile = open(f"capitalsquiz_answers{quizNum +1}.txt", "w")
                                # TODO: Dateien für Frage- und Lösungsbogen erstellen Ok
    # Schreibt den Kopf für den Test
    quizFile.write("Name:\n\nDate:\n\nPeriode:\n\n")
    quizFile.write((" "* 20) + f"State Capitals Quiz (Form {quizNum +1})")
    quizFile.write("\n\n")
                                                    # TODO: Kopf für den Test schreiben ok 
    # Würfelt die Rheinfolge der Bundesstaaten durcheinander
    states = list(capitals.keys())
    random.shuffle(states)
                        # TODO: Die Reihenfolge der Bundesstaaten durcheinanderwürfeln ok
    # Durchläuft alle 50 Staaten und erstellt eine Frage für Jedene
    for questioNum in range(50):
        correctAnswer = capitals[states[questioNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers [wrongAnswers.index(correctAnswer)] # löscht aus den ganzen Werten die richtige Antwort
        wrongAnswers = random.sample(wrongAnswers, 3) # sucht 3 Antworten aus den falschen Antworten.
        answerOptions = wrongAnswers + [correctAnswer] # liste + Liste = eine Liste ?
        random.shuffle(answerOptions) 
                # TODO: Alle 50 Staaten durchlaufen und für jeden eine Frage erstellen ok
# Schreib die Fragen und Antwort-optionem in die Quiz-Datei(quizFile).
        quizFile.write(f"{questioNum +1} Was ist die Hautpstadt von {states[questioNum]}\n")
        for i in range(4):
            quizFile.write(f"   {('ABCD'[i])}. {answerOptions[i]}\n")
        quizFile.write('\n')
                        # TODO: Fragen und mögliche Antworten in die Testdatei schreiben ok
        # Schreibt die Antwort-Schlüssel in die Datei(anwserKeyFile)
        answerKeyFile.write(f"{questioNum +1}.{"ABCD"[answerOptions.index(correctAnswer)]}\n")
    quizFile.close()
    answerKeyFile.close()