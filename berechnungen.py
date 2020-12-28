def summe_der_aktivitaeten(gespeicherten_eintraege):
    aktidict = {}
    for eintrag in gespeicherten_eintraege:
        if not aktidict.get(eintrag[0]):
            aktidict[eintrag [0]] = (eintrag [1]) = (eintrag [2])
        else:
            aktidict[eintrag [0]] += (eintrag [1])
    return aktidict