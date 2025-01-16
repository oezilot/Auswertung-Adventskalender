#------------- CODE test-beispiel --------------------------


# 0. zeile definieren:
zeile = 'i [l u v] you "too"' # für testzwecke
log_zeile = "195.234.163.46 60814 - - [01/Dec/2024:00:00:23 +0100] \"GET / HTTP/1.1\" 200 11318 \"-\" \"Zabbix\""
#print(f"Zeile im Original: {zeile}")
#print(f"Log-Zeile im Original: {log_zeile}")


# 1. Alle klammern mit gänsefüsschen ersetzen
def brack_to_gans(line):
    line = line.replace("[", '"')  # Ersetze [ mit "
    line = line.replace("]", '"')  # Ersetze ] mit "
    return line
zeile_ohne_klammern = brack_to_gans(zeile)
log_zeile_ohne_klammern = brack_to_gans(log_zeile)
#print(f"Zeile mit Gänsefüsschen statt Klammern: {zeile_ohne_klammern}")
#print(f"Log-Zeile mit Gänsefüsschen statt Klammern: {log_zeile_ohne_klammern}")


# 2. das parse-muster machen mit gänsefüsschen
def find_klammer(string):
    counter = 0
    muster = []
    klammer = False
    for buchstabe in string:
        if buchstabe == '"':            
            muster.append(8)
            if counter == 1:
                klammer = False
            else:
                klammer = True
            counter = counter + 1
        elif klammer:
            muster.append(1)
        elif not klammer:
            muster.append(0)
    return muster
klammermuster = find_klammer(zeile_ohne_klammern)
log_klammermuster = find_klammer(log_zeile_ohne_klammern)
#print(f"Klammermuster: {klammermuster}")
#print(f"Klammermuster: {log_klammermuster}")


# 3: intervalle definieren in denen sich eine klammer befindet
def set_comma_interval(parse_pattern):
    intervals = [] # array mit allen intervallen der klammern drin!    
    parse_pattern_index = -1
    klammer = False
    klammer_index = -1
    for trace in parse_pattern:
        parse_pattern_index = parse_pattern_index + 1
        if trace == 8:
            if klammer: # ende des intervals
                intervals[klammer_index]["ende"] = parse_pattern_index
                klammer = False
            else: # start des intervals
                klammer_index = klammer_index + 1
                intervals.append({"start": parse_pattern_index})  # Füge ein neues Intervall hinzu                
                klammer = True
    return intervals
klammer_intervall = set_comma_interval(klammermuster)
log_klammer_intervall = set_comma_interval(log_klammermuster)
#print(f"Klammerintervall: {klammer_intervall}")
#print(f"Klammerintervall: {log_klammer_intervall}")


# 4: alle abstände des strings mit kommas ersetzen! (das könnte man auch machen indem man den string zuerst in eine liste vewandelt und dann etwa so macht:  if line_list[i] == " ": (enter)line_list[i] = ",")
def space_to_symbol_to_comma(zeile, intervals_dict):
    zeile = zeile.replace(" ", "?")
    # alle ? innerhalb der klammern mit space ersetzen!
    for interval in intervals_dict:
        for i in range(interval["start"], interval["ende"]):
            if zeile[i] == "?":
                zeile = zeile[:i] + " " + zeile[i+1:]
    zeile = zeile.replace("?", ",")
    return zeile
fertige_zeile = space_to_symbol_to_comma(zeile_ohne_klammern, klammer_intervall)
fertige_log_zeile = space_to_symbol_to_comma(log_zeile_ohne_klammern, log_klammer_intervall)
#print(f"Fertige Zeile: {fertige_zeile}")
#print(f"Fertige Zeile: {fertige_log_zeile}")


# (main-funktion konstruieren!) eine logzeile zu einer csv-zeile konvertieren!
def log_line_to_csv_line(zeile):

    # originalzeile
    #print(f"Log-Zeile im Original: {zeile}")

    # zeile ohne klammern
    log_zeile_ohne_klammern = brack_to_gans(zeile)
    #print(f"Log-Zeile mit Gänsefüsschen statt Klammern: {log_zeile_ohne_klammern}")

    # muster zum parsen
    log_klammermuster = find_klammer(log_zeile_ohne_klammern)
    #print(f"Klammermuster: {log_klammermuster}")

    # intervall dictionary mit den intervallen der klammern innerhalb der gänsefüsschen
    log_klammer_intervall = set_comma_interval(log_klammermuster)
    #print(f"Klammerintervall: {log_klammer_intervall}")

    # fertige logzeil mit kommas getrennt und gänsefüsschen dort wo es abstände und komma zusammen gehört
    fertige_log_zeile = space_to_symbol_to_comma(log_zeile_ohne_klammern, log_klammer_intervall)
    print(f"Fertige Zeile: {fertige_log_zeile}")

    return fertige_log_zeile

print(log_line_to_csv_line(log_zeile))


# mehrere zeilen zu csv-zeilen umwandelt parat um dann das csv-file zu konstruieren! (I: log-file, O: csv-file)
log_file = open("small_log.log", "r")
log_file2 = open("filtered_advent.log", "r")


def log_file_to_csv_file(file):
    csv_liste = []
    file_line_list = file.readlines()
    for line in file_line_list:
        line = log_line_to_csv_line(line)
        csv_liste.append(line)
    return csv_liste

csv_lines_list = log_file_to_csv_file(log_file2)
#print(f"Linien im csv-Format: {csv_lines_list}")


# csv-file erstellen:
def write_csv_file(liste):
    with open("filtered_advent_log.csv", "w") as file:
        file.writelines(liste)
        print("Das File wurde unter den Namen 'advent_log_csv' erstellt oder es existiert bereits!")
write_csv_file(csv_lines_list)


# main-funktion
def log_to_csv(file):
    csv_lines_list = log_file_to_csv_file(file)
    write_csv_file(csv_lines_list)
#log_to_csv(log_file2)