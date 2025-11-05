Super Beispiel! 😊
Die Funktion `printPicnic` ist eine tolle Übung für **formatierte String-Ausgaben**, **Ausrichtung** und **Formatierungstabellen** in Python.
Hier sind **weitere Übungsaufgaben**, die denselben Themenbereich vertiefen — von leicht bis fortgeschritten:

---

## 🧩 **1. Menükarte drucken**

**Aufgabe:**
Schreibe eine Funktion `printMenu(menu: dict, left_width: int, right_width: int)`,
die ein Menü mit Gerichten und Preisen schön formatiert ausgibt.

**Beispiel:**

```python
menu = {'Pizza Margherita': 7.50, 'Lasagne': 9.00, 'Tiramisu': 4.50, 'Espresso': 2.00}
printMenu(menu, 20, 6)
```

**Ausgabe:**

```
-------- MENU --------
Pizza Margherita.....  7.50 €
Lasagne...............  9.00 €
Tiramisu..............  4.50 €
Espresso..............  2.00 €
-----------------------
```

👉 **Tipp:** Nutze `ljust()`, `rjust()` und f-Strings für die Formatierung.

---

## 📊 **2. Punktestand-Tabelle**

**Aufgabe:**
Erstelle eine Funktion `printScores(scores: dict)`, die Spielernamen und ihre Punkte tabellarisch darstellt.
Die Tabelle soll eine Kopfzeile und eine Linientrennung enthalten.

**Beispiel:**

```python
scores = {'Alice': 2500, 'Bob': 1870, 'Carla': 3250}
printScores(scores)
```

**Ausgabe:**

```
PLAYER         SCORE
---------------------
Alice          2500
Bob            1870
Carla          3250
```

👉 **Zusatz:** Verwende `.center()` für Überschriften.

---

## 💰 **3. Preisliste mit Ausrichtung**

**Aufgabe:**
Schreibe eine Funktion `printPriceList(items: list[tuple[str, float]])`,
die eine Liste von `(Artikel, Preis)`-Tupeln schön ausgibt, sodass die Kommas untereinander ausgerichtet sind.

**Beispiel:**

```python
items = [('Brot', 2.5), ('Butter', 1.25), ('Käse', 3.99), ('Milch', 1.1)]
printPriceList(items)
```

**Ausgabe:**

```
Brot    :   2.50 €
Butter  :   1.25 €
Käse    :   3.99 €
Milch   :   1.10 €
```

👉 **Tipp:** Verwende format strings wie `f"{preis:>6.2f}"` für Zahlen.

---

## 📅 **4. Kalender-Wochenübersicht**

**Aufgabe:**
Schreibe `printWeekSchedule(schedule: dict)`,
die eine Wochenübersicht formatiert ausgibt, wobei jeder Tag auf 10 Zeichen begrenzt ist.

**Beispiel:**

```python
schedule = {'Montag': 'Sport', 'Dienstag': 'Arbeit', 'Mittwoch': 'Uni', 'Donnerstag': 'Ruhetag', 'Freitag': 'Feierabend'}
printWeekSchedule(schedule)
```

**Ausgabe:**

```
Montag    | Sport
Dienstag  | Arbeit
Mittwoch  | Uni
Donnerstag| Ruhetag
Freitag   | Feierabend
```

---

## 🧾 **5. Dynamische Tabelle mit Spaltenbreiten**

**Aufgabe:**
Erstelle eine Funktion `printTable(table: list[list[str]])`,
die eine Tabelle von Strings so ausgibt, dass jede Spalte **automatisch** an die längste Zelle angepasst wird.

**Beispiel:**

```python
tableData = [
    ['Apfel', 'Banane', 'Kirsche'],
    ['Rot', 'Gelb', 'Rot'],
    ['1.2€', '0.9€', '3.5€']
]
printTable(tableData)
```

**Ausgabe:**

```
Apfel  Banane  Kirsche
Rot    Gelb    Rot
1.2€   0.9€    3.5€
```

👉 **Tipp:**

1. Berechne für jede Spalte die maximale Breite.
2. Richte mit `.rjust()` oder `.ljust()` aus.

---

## 🧠 **Bonus: Tabellen mit Zahlen und Prozenten**

**Aufgabe:**
Schreibe `printStats(data: list[tuple[str, int, int]])`,
die eine Statistik-Tabelle mit Prozenten darstellt.

**Beispiel:**

```python
data = [('Alice', 45, 50), ('Bob', 38, 50), ('Clara', 49, 50)]
printStats(data)
```

**Ausgabe:**

```
Name     | Punkte | Prozent
----------------------------
Alice    | 45/50  | 90.0%
Bob      | 38/50  | 76.0%
Clara    | 49/50  | 98.0%
```

👉 **Tipp:** Prozent = `(erreicht / max) * 100`.

---

Möchtest du, dass ich dir **Lösungen (mit Beispielcode)** zu diesen Aufgaben generiere — z. B. als Lernpaket zum Durcharbeiten?
Ich kann sie nummeriert mit Erklärungen und Tests liefern.
