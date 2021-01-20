def summe_der_uebung(gespeicherten_eintraege):
    aktidict = {}
    for eintrag in gespeicherten_eintraege:
        if not aktidict.get(eintrag['uebung']):
            aktidict[eintrag['uebung']] = (eintrag['kilo'])
        else:
            aktidict[eintrag['uebung']] += (eintrag['kilo'])
        return aktidict


