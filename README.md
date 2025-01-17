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
Summe aller Aufrufe vom 1. bis 24. Dezember: 1318
Summe aller Aufrufe ab dem 25 Dezember: 113
```

## Fragen für die Statistik
daten kennenlernen:
- erkenntnis: je nach frage ein anderes datenset und eine andere graphik
- was heissen die verschiedenen kolonnen?
- so sieht ein request aus wenn jemand dann den filmlink klickt: (um die logs für diese links ansehen zu können muss ich wohl das logfile für die nanoo-seite bekommen...momentan habe ich nur die logs der portalseite!)
```bash
https://www.nanoo.tv/link/v/799061 (die nummer am schluss variiert von film zu film!)
```
- wie erkennt man dass eine person die website besucht hat? was ist ein besuch?
- was heisst es beim sdventskalenderbesuch wenn kein url eingegeben wurde?
- wie kann man personen eindeutig identifiziern? kann amn das überhaupt?
- wenn eine person eine aktion durchführt auf der seite wie einen button zu klicken...gibt es dafür eine neue logzeile? kann ich in den logs sehen wenn jemand auf einen link gedrückt hat? oder sieht das nur die firma der das target dieser links gehört?
- wie sieht eine zeile aus der logdaten wenn jemand einen filmlink des adventskalenders aufruft?
- wie sehen die logdaten für einen kalenderaufruf aus?
   ```bash
   2a02:1210:861f:600:9447:ad6e:b7:54fa 55076 - - [01/Dec/2024:00:17:51 +0100] "GET /adventskalender/slideshow.html HTTP/1.1" 200 9536 "https://www.nanoo.tv/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1.1 Safari/605.1.15"
   2a02:1210:861f:600:9447:ad6e:b7:54fa 55076 - - [01/Dec/2024:00:17:51 +0100] "GET /adventskalender/slideshow.css HTTP/1.1" 200 7134 "https://portal.nanoo.tv/adventskalender/slideshow.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1.1 Safari/605.1.15"
   2a02:1210:861f:600:9447:ad6e:b7:54fa 55077 - - [01/Dec/2024:00:17:51 +0100] "GET /adventskalender/slideshow.js HTTP/1.1" 200 12672 "https://portal.nanoo.tv/adventskalender/slideshow.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1.1 Safari/605.1.15"
   2a02:1210:861f:600:9447:ad6e:b7:54fa 55077 - - [01/Dec/2024:00:17:51 +0100] "GET /adventskalender/Logo_werft22.png HTTP/1.1" 200 27224 "https://portal.nanoo.tv/adventskalender/slideshow.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1.1 Safari/605.1.15"
   2a02:1210:861f:600:9447:ad6e:b7:54fa 55076 - - [01/Dec/2024:00:17:51 +0100] "GET /adventskalender/Tree.png HTTP/1.1" 200 3493745 "https://portal.nanoo.tv/adventskalender/slideshow.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1.1 Safari/605.1.15"
   2a02:1210:861f:600:9447:ad6e:b7:54fa 55077 - - [01/Dec/2024:00:17:52 +0100] "GET /adventskalender/previous.png HTTP/1.1" 200 12052 "https://portal.nanoo.tv/adventskalender/slideshow.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1.1 Safari/605.1.15"
   2a02:1210:861f:600:9447:ad6e:b7:54fa 55077 - - [01/Dec/2024:00:17:52 +0100] "GET /adventskalender/weihnachtskranz.png HTTP/1.1" 200 75020 "https://portal.nanoo.tv/adventskalender/slideshow.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1.1 Safari/605.1.15"
   2a02:1210:861f:600:9447:ad6e:b7:54fa 55077 - - [01/Dec/2024:00:17:52 +0100] "GET /favicon.ico HTTP/1.1" 404 1460 "https://portal.nanoo.tv/adventskalender/slideshow.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1.1 Safari/605.1.15"
   ```

Welche Daten (Kolonnen) sind wichtig?
- url (nur die zeilen mit dem eingeben des adventkanleder links)
- requests (nur die requests auf die aventskalenderseite)
- datum

einfache fragen:
- Total anz. Aufrufe 
- Aufrufe für jeden Tag
- Durchschnittliche Anzahl Aufrufe

schwierige fragen:
- Wie viele der Aufrufe haben dann auch die filme geschaut (wie viele haben auf den filmlink gedrück und dann mind so ca 30min auf diesem link verbracht? wie viele user mit dem selben usernamen habe den film geschaut und den kalender angesehen?)

zusatzfragen:
- Wie viele unique Besucher
- welcher film wurde am meisten aufgerufen?
- wie viele besucher sind auch auf die contributers seite gegangen
- wie viele haben den link zum film gedrückt 
- wie viele haben irgendeinen link gedrückt
- Regelmässige besucher...gibt es jemand der jeden Tag ein törchen geöffnet hat, wer hat am meisten töcrhen besucht?
- wie viele nanoo-user/wie viele nicht-user haben die seite bescuht

## Ressourcen
link zur visualisierung der daten: https://code.visualstudio.com/docs/datascience/data-science-tutorial

## Einen Blick auf die Log-Daten
was ist ein log?

struktur eines logs:

wie werte ich das log aus?
hier sind logadaten pro aufruf der website:
```bash
```
## Schwierigkeitem
- man muss immer schauen dass es immer daten für alles gibt!

## Daten verschönern
1. aus dem logfile ein csv machen!
   - csv -> mit kommas werden neue kolonnen unterschieden und mit enters eine neue zeile

!!! jeder abstand ist eine neue kolonnenwand ausser für den content der sich innerhalb von [] oder "" befindet !!!

1. jypyter notebook

## Graphiken machen Schritt für Schritt:
1. Graphik welche die Aufrufe des Kalenders veranschaulicht während den dezembertagen (datensatz: gefilterte daten anz. zeilen)
   1. maximum und minimum
   2. durchschnitt während dem dezember
   3. totalaufrufe
2. um welche uhrzeit geschaut
   1. max min und durchschnitt
   2. max stunden auf der website verbracht
3. wie viele unique nutzer?

## Links
- dynamische graphiken: https://quickchart.io/documentation/ 
- 

## Autorin
Zoé Flumini