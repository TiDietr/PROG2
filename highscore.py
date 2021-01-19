import json

import shelve

scoreFile = shelve.open('tracker.json')

def updateScore(newScore):
  if('uebung' in scoreFile):
    uebung = scoreFile['uebung']
    if(newUebung not in uebung):
      uebung.insert(0, newUebung)

    uebung.sort()
    ranking = uebung.index(newUebung)
    ranking = len(uebung)-ranking
  else:
    Uebung = [newUebung]
    gewicht = gewicht

  print(uebung)
  print(gewicht)
  scoreFile['uebung'] = uebung
  return ranking

newScore = int(input("New HighScore: \n"))
updateScore(newScore)