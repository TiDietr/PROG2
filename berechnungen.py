def summe_der_uebung(gespeicherten_eintraege):
    aktidict = {}
    for eintrag in gespeicherten_eintraege:
        if not aktidict.get(eintrag['uebung']):
            aktidict[eintrag['uebung']] = float(eintrag['kilo'])
        else:
            aktidict[eintrag['uebung']] += float(eintrag['kilo'])
        return aktidict


