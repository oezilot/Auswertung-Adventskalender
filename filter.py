'''
todo:
- log-file schöner darstellen
- logfile reduzieren auf get-request auf die website slideshow
- datenbank (unique visitors, pro tag, überhaupt, ...)
- das ganze in elm machen?! mit den types etc...

-> ich stelle das log wie in einer tabelle dar!!!

bestandteile eines logs:
- ip-adresse des nutzers 
- port des nutzers
- logindaten oder - -
- datum (in eckigen klammern)
- http-request (in gänsefüsschen)
- http-response (z.b 200)
- port des ausgangs?
- - (gänsefüsschen)
- broser wo der request gemacht wurde

'''

# file mit allen logs hineinladen
log_file = open("advent.log", "r")
log_file_line_list = log_file.readlines()
#print(log_file_line_list[88])

# filter-funktion welce bei einer zeil erkent ob diese zum adventskalender-aufruf gehört
def check_line(line):
    splitted_line = line.split()

    if splitted_line[7] == "/adventskalender/slideshow.html":
        return True
    else:
        return False

# filter angewendet (loop der den die filterfunktion von mir auf jede zeile anwendet im logfile!)
advent_line_list = list(filter(check_line, log_file_line_list))
#print(advent_line_list[88])


# überprüfen ob eine logzeile am tag x entstanden ist
def check_day(line, day):
    day_of_line = line.split("[")
    day_of_line = int(day_of_line[1][:2])
    if day_of_line == day:
        return True
    else:
        return False

# logs von einem gewissen tag herausfinden
def get_lines_for_day(day):
    logs_of_day = list(filter(lambda x:check_day(x, day), advent_line_list))
    return logs_of_day


#---------- DATEN FÜR DIE STATISTIK ------------

# total aufrufe des adventskalenders 
print(f"Aufrufe Total: {len(advent_line_list)}")

# anzahl logaufrufe an irgendeinem tag (hier: 5)
def get_number_of_calls_for_day(day):
    return len(get_lines_for_day(day))
print(f"Anzahl Aufrufe am Tag 1: {get_number_of_calls_for_day(1)}")

# summe aller aufrufe während tagen von tag 1 bis tag 24 und einzelne aufrufe jeden tag
summe = 0
for i in range(1, 25):
    summe = summe + get_number_of_calls_for_day(i)
    print(f"Anzahl Aufrufe am Tag {i}: {get_number_of_calls_for_day(i)}")
print(f"Summe aller Aufrufe vom 1. bis 14. Dezember: {summe}")

# summe aller aufrufe ausserhalb der weihnachstzeit:
print(f"Summe aller Aufrufe ab dem 25 Dezember: {len(advent_line_list) - summe}")



    

# durchschnittlichhe aufrufe pro tag

# neues file mit gefilterter info speichern
#open("filtered_advent.log", "w").writelines(advent_line_list)
