## 🧩 Arbeiten mit **benannten Gruppen** in Regex und **`re.sub()`** in Python  
Eine kompakte, aber gründliche Doku, die dir zeigt, wie du:

- benannte Gruppen definierst  
- sie in `re.sub()` verwendest  
- Gruppen ersetzt, neu anordnest oder gegeneinander tauschst  

---

## 🎯 1. Benannte Gruppen in Python-Regex  
Benannte Gruppen machen reguläre Ausdrücke lesbarer.  
Die Syntax lautet:

```python
(?P<gruppenname>regex)
```

Beispiel: Vor- und Nachname extrahieren:

```python
pattern = r"(?P<vorname>\w+)\s+(?P<nachname>\w+)"
```

---

## 🔄 2. Benannte Gruppen in `re.sub()` verwenden  
In `re.sub()` kannst du benannte Gruppen über **`\g<gruppenname>`** referenzieren.

### Beispiel: Reihenfolge tauschen (Nachname, Vorname → Vorname Nachname)

```python
import re

text = "Müller, Hans"
pattern = r"(?P<nachname>\w+),\s*(?P<vorname>\w+)"

result = re.sub(pattern, r"\g<vorname> \g<nachname>", text)
print(result)
```

**Ausgabe:**

```
Hans Müller
```

---

## 🛠️ 3. Gruppen ersetzen  
Du kannst einzelne Gruppen gezielt verändern oder ersetzen.

### Beispiel: Nur den Vornamen ersetzen

```python
text = "Hans Müller"
pattern = r"(?P<vorname>\w+)\s+(?P<nachname>\w+)"

result = re.sub(pattern, r"Peter \g<nachname>", text)
print(result)
```

**Ausgabe:**

```
Peter Müller
```

---

## 🔁 4. Gruppen tauschen  
Das Tauschen ist einfach ein Re-Mapping der Gruppen im Replacement-String.

### Beispiel: Tag-Monat-Jahr → Jahr-Monat-Tag

```python
text = "31-12-2024"
pattern = r"(?P<tag>\d{2})-(?P<monat>\d{2})-(?P<jahr>\d{4})"

result = re.sub(pattern, r"\g<jahr>-\g<monat>-\g<tag>", text)
print(result)
```

**Ausgabe:**

```
2024-12-31
```

---

## 🧠 5. Replacement per Funktion (für komplexere Logik)  
Wenn du nicht nur umsortieren, sondern **berechnen oder transformieren** willst, kannst du eine Funktion an `re.sub()` übergeben.

### Beispiel: Namen großschreiben

```python
def format_name(match):
    vor = match.group("vorname").capitalize()
    nach = match.group("nachname").upper()
    return f"{vor} {nach}"

text = "hans müller"
pattern = r"(?P<vorname>\w+)\s+(?P<nachname>\w+)"

result = re.sub(pattern, format_name, text)
print(result)
```

**Ausgabe:**

```
Hans MÜLLER
```

---

## 📘 6. Übersicht der wichtigsten Syntaxelemente

| Zweck | Syntax | Beispiel |
|------|--------|----------|
| Benannte Gruppe | `(?P<name>...)` | `(?P<tag>\d{2})` |
| Gruppe referenzieren | `\g<name>` | `\g<tag>` |
| Replacement-Funktion | `re.sub(pattern, func, text)` | `format_name()` |

---

## 🚀 Wenn du willst, erweitere ich die Doku  
Zum Beispiel um:

- Beispiele mit optionalen Gruppen  
- Lookaheads/Lookbehinds  
- Validierung komplexer Strings (Emails, URLs, Datumsformate)  
- Performance-Tipps für Regex in Python  

Sag einfach Bescheid, was du brauchst.
