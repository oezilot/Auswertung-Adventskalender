# Auswertung Adventskalender 2025

## Installation des Skripts
```bash
```

## Wichtige Variablen
```python
```

## Daten für die Statistiken

```python
# total aufrufe des adventskalenders 
print(f"Aufrufe Total: {len(advent_line_list)}")

# anzahl logaufrufe an irgendeinem tag (hier: 5)
def get_number_of_calls_for_day(day):
    return len(get_lines_for_day(day))
print(f"Anzahl Aufrufe am Tag 5: {get_number_of_calls_for_day(5)}")

# summe aller aufrufe während tagen von tag 1 bis tag 24 und einzelne aufrufe jeden tag
summe = 0
for i in range(0, 1):
    summe = summe + get_number_of_calls_for_day(i)
    print(f"Anzahl Aufrufe am Tag {i}: {get_number_of_calls_for_day(i)}")
print(f"Summe aller Aufrufe vom 1. bis 14. Dezember: {summe}")
```

## Resultete der Statistik
```bash
Aufrufe Total: 1431
Anzahl Aufrufe am Tag 1: 73
Anzahl Aufrufe am Tag 1: 73
Anzahl Aufrufe am Tag 2: 90
Anzahl Aufrufe am Tag 3: 88
Anzahl Aufrufe am Tag 4: 74
Anzahl Aufrufe am Tag 5: 77
Anzahl Aufrufe am Tag 6: 79
Anzahl Aufrufe am Tag 7: 54
Anzahl Aufrufe am Tag 8: 57
Anzahl Aufrufe am Tag 9: 46
Anzahl Aufrufe am Tag 10: 68
Anzahl Aufrufe am Tag 11: 66
Anzahl Aufrufe am Tag 12: 59
Anzahl Aufrufe am Tag 13: 48
Anzahl Aufrufe am Tag 14: 41
Anzahl Aufrufe am Tag 15: 42
Anzahl Aufrufe am Tag 16: 55
Anzahl Aufrufe am Tag 17: 61
Anzahl Aufrufe am Tag 18: 47
Anzahl Aufrufe am Tag 19: 60
Anzahl Aufrufe am Tag 20: 39
Anzahl Aufrufe am Tag 21: 27
Anzahl Aufrufe am Tag 22: 27
Anzahl Aufrufe am Tag 23: 22
Anzahl Aufrufe am Tag 24: 18
Summe aller Aufrufe vom 1. bis 14. Dezember: 1318
Summe aller Aufrufe ab dem 25 Dezember: 113
```

## Fragen für die Statistik
einfache fragen:
- Total anz. Aufrufe 
- Aufrufe für jeden Tag
- Durchschnittliche Anzahl Aufrufe

schwierige fragen:
- Wie viele der Aufrufe haben dann auch die filme geschaut

zusatzfragen:
- Wie viele unique Besucher
- Regelmässige besucher...gibt es jemand der jeden Tag ein törchen geöffnet hat, wer hat am meisten töcrhen besucht?
- wie viele nanoo-user/wie viele nicht-user haben die seite bescuht

## Ressourcen
link zur visualisierung der daten: https://code.visualstudio.com/docs/datascience/data-science-tutorial

## Autorin
Zoé Flumini