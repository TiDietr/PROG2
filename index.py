import json

def bmispeichern(bmi): #speichern in json

    try:
        with open("bmi.json", "r") as datenbank:
         eintraege = json.load(datenbank)
    except:
        eintraege = []


    eintrag = {
    'bmi': bmi



    }

    eintraege.append(eintrag)

    with open("bmi.json", "w") as datenbank:
        json.dump(eintraege, datenbank)

    return bmi


def bmiladen(): #laden von json für andere Seite
    try:
        with open("termin.json", "r") as datenbank:
         eintraege = json.load(datenbank)
    except:
        print('Beim laden konnte keine vorhandene Datenbank gefunden werden')
        eintraege = []

    return eintraege

def status(bmi): #Berechnung BMI
    if bmi < 18.5:
        return 'Du bist untergewichtig.'

    elif 18.5 <= bmi < 25:
        return 'Du bist normalgewichtig.'

    elif bmi > 25:
        return 'Du bist übergewichtig.'
    else:
        return 'Etwas ist schiefgelaufen versuch es nochmals. Achtung Grösse in Meter und Gewicht in KG!'





