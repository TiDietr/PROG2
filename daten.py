import json
from typing import TextIO


def speichern(aktivitaet, gewicht, wiederholung):

    try:
        with open("datenbank.json", "r") as datenbank:
         eintraege = json.load(datenbank)
    except:
        eintraege = []

    eintrag =(aktivitaet, gewicht, wiederholung)

    eintraege.append(eintrag)

    with open("datenbank.json", "w") as datenbank:
        json.dump(eintraege, datenbank)

    return "Daten gespeichert"