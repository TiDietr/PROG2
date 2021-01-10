import json
from typing import TextIO


def speichern(uebung, gewicht, wiederholung):

    try:
        with open("tracker.json", "r") as datenbank:
         eintraege = json.load(datenbank)
    except:
        eintraege = []

    eintrag =(uebung, gewicht, wiederholung)

    eintraege.append(eintrag)

    with open("tracker.json", "w") as datenbank:
        json.dump(eintraege, datenbank)

    return uebung, gewicht, wiederholung