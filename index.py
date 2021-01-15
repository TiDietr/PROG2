from flask import Flask
from flask import render_template,url_for,redirect

def status(bmi):
    if bmi < 18.5:
        return 'Du bist untergewichtig öffne diesen Link zu deinem Trainingsplan:'

    elif 18.5 <= bmi < 25:
        return 'Du bist normalgewichtig öffne diesen Link zu deinem Trainingsplan:'

    elif bmi > 25:
        return 'Du bist übergewichtig öffne diesen Link zu deinem Trainingsplan:'
    else:
        return 'Etwas ist schiefgelaufen versuch es nochmals.'





