from flask import Flask
from flask import render_template,url_for,redirect

def status(bmi):
    if bmi < 18.5:
        return 'Du bist untergewichtig.'

    elif 18.5 <= bmi < 25:
        return 'Du bist normalgewichtig.'

    elif bmi > 25:
        return 'Du bist übergewichtig.'
    else:
        return 'Etwas ist schiefgelaufen versuch es nochmals. Achtung Grösse in Meter und Gewicht in KG!'





