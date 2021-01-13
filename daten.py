import json
from typing import TextIO


def speichern(name, ziel,telefonnummer,alter,groesse,gewicht, datum, zeit):

    try:
        with open("termin.json", "r") as datenbank:
         eintraege = json.load(datenbank)
    except:
        eintraege = []

    eintrag =(name, ziel,telefonnummer,alter,groesse,gewicht, datum, zeit)

    eintraege.append(eintrag)

    with open("termin.json", "w") as datenbank:
        json.dump(eintraege, datenbank)

    return name, ziel,telefonnummer,alter,groesse,gewicht, datum, zeit


def laden():
    try:
        with open("termin.json", "r") as datenbank:
         eintraege = json.load(datenbank)
    except:
        print('Beim laden konnte keine vorhandene Termine in der Datenbank gefunden werden')
        eintraege = []

    return eintraege