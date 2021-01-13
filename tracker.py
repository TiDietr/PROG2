import json
def speichern1(uebung, wiederholungen, gewicht):

    try:
        with open("tracker.json", "r") as datenbank:
         eintraege = json.load(datenbank)
    except:
        eintraege = []

    eintrag =(uebung, wiederholungen, gewicht)

    eintraege.append(eintrag)

    with open("tracker.json", "w") as datenbank:
        json.dump(eintraege, datenbank)

    return uebung, wiederholungen, gewicht
