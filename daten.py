import json
from datetime import datetime

def speichern(name, ziel,telefon,alter,groesse,gewicht, tag, zeit):

    try:
        with open("termin.json", "r") as datenbank:
         eintraege = json.load(datenbank)
    except:
        eintraege = []

    #datum = str(datetime.now())
    eintrag = {
        'tag': tag,
        'zeit': zeit,
        'ziel': ziel,
        'name': name,
        'telefon': telefon,
        'alter': alter,
        'groesse': groesse,
        'gewicht': gewicht,

    }

    eintraege.append(eintrag)

    with open("termin.json", "w") as datenbank:
        json.dump(eintraege, datenbank)

    return name, ziel,telefon,alter,groesse,gewicht, datum, zeit


def laden():
    try:
        with open("termin.json", "r") as datenbank:
         eintraege = json.load(datenbank)
    except:
        print('Beim laden konnte keine vorhandene Datenbank gefunden werden')
        eintraege = []

    return eintraege



