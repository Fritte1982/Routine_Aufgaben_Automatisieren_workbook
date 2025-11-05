Perfekt! 😊 Hier ist eine Sammlung von **Übungsaufgaben speziell zum Thema „Tabellen, Schleifen, Zeilen/Spalten, Spaltenbreiten, formatierte Ausgabe“** in Python. Ich gestalte sie so, dass sie **anfängerfreundlich starten und dann fortgeschrittene Aspekte** abdecken.

---

## **Teil 1: Einfache Zeilen-Iteration**

**Aufgabe 1:**
Gegeben ist eine Liste von Listen:

```python
data = [
    ['Alice', 24, 'Berlin'],
    ['Bob', 30, 'Hamburg'],
    ['Clara', 22, 'München']
]
```

* Schreibe eine Funktion `print_rows(data)`, die jede Zeile auf einer neuen Zeile ausgibt.
* Nutze eine Schleife über **Zeilen** und dann eine Schleife über die **Elemente der Zeile**.

**Erwartete Ausgabe:**

```
Alice 24 Berlin
Bob 30 Hamburg
Clara 22 München
```

---

**Aufgabe 2:**
Erweitere Aufgabe 1, sodass:

* Zahlen rechtsbündig (z. B. `24`, `30`) in **5 Zeichen Breite** stehen
* Strings linksbündig in **10 Zeichen Breite** stehen

**Tipp:** Verwende f-Strings und `.ljust()` / `.rjust()`.

---

## **Teil 2: Spaltenbreiten berechnen**

**Aufgabe 3:**
Gegeben ist:

```python
table = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]
```

* Berechne eine Liste `column_widths`, die die **maximale Länge jedes Elements pro Spalte +1** enthält.
* Schreibe eine Funktion `compute_column_widths(table)`.

**Tipp:** Iteriere über Spaltenindizes und für jede Spalte über die Zeilen.

---

**Aufgabe 4:**
Nutze `column_widths` aus Aufgabe 3, um eine **schöne Tabelle** auszugeben:

```
apples  oranges cherries banana
Alice   Bob     Carol    David
dogs    cats    moose    goose
```

* Jede Spalte soll **breit genug sein**, um das längste Element aufzunehmen.
* Nutze `.ljust()` für die Strings.

---

## **Teil 3: Fortgeschritten – formatiert mit Zahlen**

**Aufgabe 5:**
Erstelle eine Funktion `print_scores(scores: dict)`:

```python
scores = {'Alice': 2500, 'Bob': 1870, 'Clara': 3250}
```

* Ausgabe in zwei Spalten: Name links, Score rechts
* Name: linksbündig, 12 Zeichen
* Score: rechtsbündig, 6 Zeichen

**Erwartete Ausgabe:**

```
Alice       2500
Bob         1870
Clara       3250
```

---

**Aufgabe 6:**
Tabelle mit Preisen:

```python
items = [('Brot', 2.5), ('Butter', 1.25), ('Käse', 3.99)]
```

* Schreibe `print_price_list(items)`
* Ausgabe: `Item : Preis €`, zwei Nachkommastellen, Preis rechtsbündig in 6 Zeichen

**Beispiel:**

```
Brot   :   2.50 €
Butter :   1.25 €
Käse   :   3.99 €
```

---

## **Teil 4: Optional – Bonus**

**Aufgabe 7:**
Schreibe `transpose(table)`:

* Wandelt Zeilen in Spalten um und gibt die transponierte Tabelle zurück
* Teste mit:

```python
table = [
    ['a', 'b', 'c'],
    ['1', '2', '3']
]
```

**Erwartetes Ergebnis:**

```
[['a', '1'], ['b', '2'], ['c', '3']]
```

**Ziel:** Übung für **Spaltenzugriff mit Indizes**.

---

**Aufgabe 8:**
Erstelle eine Funktion `print_table(table)`:

* Automatisch **Spaltenbreiten berechnen**
* Tabelle sauber ausgeben, **zentriert oder rechts/links ausgerichtet**
* Bonus: Kopfzeile und Trennlinie (`-`)

---

Wenn du willst, kann ich dir jetzt **die Lösungen mit fertigem Python-Code** zu allen Aufgaben schreiben – **inklusive Kommentare**, sodass du direkt testen und verstehen kannst.

Willst du, dass ich das mache?
