Perfekt 👍 — hier kommt eine **kompakte, aber vollständige Übersicht** der wichtigsten **Format-Optionen für f-Strings** (und `format()` in Python).
Damit kannst du alles von **Ausrichtung** über **Nachkommastellen** bis zu **Zahlendarstellung** schnell nachschlagen.

---

## 🧩 **Grundsyntax**

```python
f"{wert:[Ausrichtung][Füllzeichen][Breite][.Präzision][Typ]}"
```

**Beispiel:**

```python
f"{3.14159:>8.2f}"
```

➡️ Rechtsbündig (`>`), Gesamtbreite 8, 2 Nachkommastellen, Fließkommazahl (`f`)
**Ausgabe:** `'    3.14'`

---

## 📐 **1. Ausrichtung & Füllzeichen**

| Format | Bedeutung                 | Beispiel            | Ausgabe        |
| ------ | ------------------------- | ------------------- | -------------- |
| `>10`  | rechtsbündig              | `f"{'Apfel':>10}"`  | `'     Apfel'` |
| `<10`  | linksbündig               | `f"{'Apfel':<10}"`  | `'Apfel     '` |
| `^10`  | zentriert                 | `f"{'Apfel':^10}"`  | `'  Apfel  '`  |
| `*^10` | zentriert mit Füllzeichen | `f"{'Apfel':*^10}"` | `'**Apfel***'` |

---

## 🔢 **2. Feldbreite**

| Syntax | Bedeutung                 | Beispiel     | Ausgabe    |
| ------ | ------------------------- | ------------ | ---------- |
| `:6`   | Feld mit 6 Zeichen Breite | `f"{42:6}"`  | `'    42'` |
| `:<6`  | Links ausgerichtet        | `f"{42:<6}"` | `'42    '` |
| `:^6`  | Zentriert                 | `f"{42:^6}"` | `' 42  '`  |

---

## 💰 **3. Nachkommastellen**

| Syntax | Bedeutung                   | Beispiel           | Ausgabe   |
| ------ | --------------------------- | ------------------ | --------- |
| `.2f`  | 2 Nachkommastellen (float)  | `f"{3.14159:.2f}"` | `'3.14'`  |
| `.0f`  | Ganze Zahl (ohne Nachkomma) | `f"{3.99:.0f}"`    | `'4'`     |
| `.3f`  | 3 Nachkommastellen          | `f"{2.5:.3f}"`     | `'2.500'` |

---

## 💹 **4. Zahlenformate (Typen)**

| Typ   | Bedeutung                              | Beispiel           | Ausgabe          |
| ----- | -------------------------------------- | ------------------ | ---------------- |
| `d`   | Ganzzahl (decimal)                     | `f"{42:d}"`        | `'42'`           |
| `f`   | Festkommazahl                          | `f"{3.14:f}"`      | `'3.140000'`     |
| `.2f` | Festkommazahl mit 2 Nachkommastellen   | `f"{3.14:.2f}"`    | `'3.14'`         |
| `e`   | Exponentialschreibweise                | `f"{1234:e}"`      | `'1.234000e+03'` |
| `g`   | Automatische Wahl zwischen `f` und `e` | `f"{0.0000123:g}"` | `'1.23e-05'`     |
| `,`   | Tausender-Trennzeichen                 | `f"{1234567:,}"`   | `'1,234,567'`    |
| `_`   | Tausender mit Unterstrich              | `f"{1234567:_}"`   | `'1_234_567'`    |
| `%`   | Prozent (×100 mit %-Zeichen)           | `f"{0.256:%}"`     | `'25.600000%'`   |
| `.1%` | Prozent mit 1 Nachkommastelle          | `f"{0.256:.1%}"`   | `'25.6%'`        |

---

## 💶 **5. Kombination von Breite, Ausrichtung & Nachkommastellen**

| Beispiel          | Bedeutung                                  | Ausgabe      |
| ----------------- | ------------------------------------------ | ------------ |
| `f"{12.3:>8.2f}"` | Rechtsbündig, Breite 8, 2 Nachkommastellen | `'   12.30'` |
| `f"{12.3:<8.2f}"` | Linksbündig, Breite 8                      | `'12.30   '` |
| `f"{12.3:^8.2f}"` | Zentriert, Breite 8                        | `' 12.30  '` |

---

## 🔤 **6. Strings formatieren**

| Beispiel            | Ausgabe        |
| ------------------- | -------------- |
| `f"{'Apfel':>10}"`  | `'     Apfel'` |
| `f"{'Apfel':<10}"`  | `'Apfel     '` |
| `f"{'Apfel':^10}"`  | `'  Apfel  '`  |
| `f"{'Apfel':*^10}"` | `'**Apfel***'` |

---

## 📊 **7. Zahlen mit Vorzeichen**

| Beispiel     | Ausgabe | Bedeutung                     |
| ------------ | ------- | ----------------------------- |
| `f"{+42:+}"` | `'+42'` | Immer Vorzeichen              |
| `f"{-42:+}"` | `'-42'` | Immer Vorzeichen              |
| `f"{42: }"`  | `' 42'` | Leerzeichen für positive Zahl |
| `f"{-42: }"` | `'-42'` | Negativ mit Minus             |

---

## 🧠 **8. Beispielzusammenfassung**

```python
wert = 1234.5
print(f"{wert:>10.2f}")   # Rechtsbündig, Breite 10, 2 Nachkommastellen
print(f"{wert:<10,.2f}")  # Links, Breite 10, Tausendertrennung, 2 Nachkommastellen
print(f"{wert:^12.2f}")   # Zentriert in 12 Zeichen
print(f"{wert:*>10.2f}")  # Mit Sternchen aufgefüllt
```

**Ausgabe:**

```
   1234.50
1,234.50  
  1234.50  
***1234.50
```

---

Möchtest du, dass ich dir daraus ein **schön formatiertes PDF-Spickzettel** (Cheat Sheet) generiere — perfekt zum Ausdrucken oder Lernen?
