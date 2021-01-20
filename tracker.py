import json
from datetime import datetime

def save(uebung, wiederholungen, kilo):

    try:
        with open("tracker.json", "r") as datenbank:
         eintraege = json.load(datenbank)
    except:
        eintraege = []

    datum = datetime.today().strftime('%Y-%m-%d')
    eintrag = {
        'datum': datum,
        'uebung': uebung,
        'kilo': kilo,
        'wiederholungen' : wiederholungen
    }

    eintraege.append(eintrag)

    with open("tracker.json", "w") as datenbank:
        json.dump(eintraege, datenbank)

    return uebung, wiederholungen, kilo

def tracken():
    try:
        with open("tracker.json", "r") as datenbank:
         eintraege = json.load(datenbank)
    except:
        print('Beim laden konnte keine vorhandene Datenbank gefunden werden')
        eintraege = []

    return eintraege
