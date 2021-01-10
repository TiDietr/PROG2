import json
from typing import TextIO


def speichern(name, adresse, termin):

    try:
        with open("termin.json", "r") as datenbank:
         eintraege = json.load(datenbank)
    except:
        eintraege = []

    eintrag =(name, adresse, termin)

    eintraege.append(eintrag)

    with open("termin.json", "w") as datenbank:
        json.dump(eintraege, datenbank)

    return name, adresse, termin