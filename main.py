from flask import Flask
from flask import render_template
from flask import request, json, url_for
from flask import redirect
import os
from flask import session


from daten import speichern, laden
from index import status
from tracker import save, tracken
from berechnungen import summe_der_uebung
from highscore import get_scores
import json
from views import bestaetigung

from django.shortcuts import render




app = Flask("Fitnesscoach!")



farben = {
    "Oberkoerper": "#FF0000",
    "Beine": "#0000FF",
    "Ganzkoerper": "#CCEEFF"
}

@app.route('/')
def start():
    titel_text = 'Wilkommen beim persönlichen Fitnesscoach'
    einleitungs_text = 'Hier finden Sie alles zum Thema Fitness'
    return render_template('index.html', app_name='Fitnesscoach', ueberschrift=titel_text, einleitung=einleitungs_text)


@app.route('/termin', methods=['POST','GET'])
def eingabe_formular():
    if request.method == 'POST':
        ziel = request.form['ziel']
        name = request.form['name']
        telefon = request.form['telefon']
        alter = request.form['alter']
        gewicht = request.form['gewicht']
        groesse = request.form['groesse']
        zeit = request.form['zeit']
        datum = request.form['datum']

        speichern(name, ziel,telefon,alter,groesse,gewicht, zeit, datum)
        return redirect('/bestaetigung')
    return render_template('termin.html')

@app.route('/bmi', methods=['POST','GET'])
def rechner():
    bmi=''
    berechnung=''
    if request.method == 'POST' and 'gewicht' in request.form and 'groesse' in request.form:
        gewicht=float(request.form.get('gewicht'))
        groesse=float(request.form.get('groesse'))
        bmi = round(gewicht/(groesse * groesse),2)
        berechnung=status(bmi)

    return render_template("bmi.html", bmi=bmi, berechnung=berechnung)

@app.route('/plan1')
def plan1():
    return render_template("plan1.html")

@app.route('/plan2')
def plan2():
    return render_template("plan2.html")

@app.route('/plan3')
def plan3():
    return render_template("plan3.html")







@app.route('/bestaetigung', methods=['POST','GET'])
def bestaetigung():
    if request.method == 'POST' and 'ziel' in request.form and 'name' in request.form and 'telefon' in request.form and 'alter' in request.form and 'gewicht' in request.form and 'groesse' in request.form and 'zeit' in request.form and 'datum' in request.form:
        ziel = request.form.get('ziel')
        name = request.form.get('name')
        telefon= request.form.get('telefon')
        alter= request.form.get('alter')
        gewicht= request.form.get('gewicht')
        groesse= request.form.get('groesse')
        zeit= request.form.get('zeit')
        tag= request.form.get('tag')

       # send_mail(

        #)
        speichern(name, ziel,telefon,alter,groesse,gewicht, tag, zeit)
        return render_template('bestaetigung.html' , zeil=ziel, name = name, telefon=telefon, alter=alter,gewicht=gewicht,groesse=groesse, zeit=zeit, tag=tag)
    else:
        return render_template('fehler.html')







@app.route('/tracker', methods=['POST','GET'])
def tracker():
    if request.method == 'POST':
        uebung = request.form['uebung']
        gewicht = request.form['kilo']
        wiederholungen = request.form['wiederholungen']

        save(uebung,gewicht, wiederholungen)
        return render_template('tracker1.html')
    return render_template('tracker.html')

@app.route('/trackermore', methods=['POST','GET'])
def tracker1():
    if request.method == 'POST':
        uebung = request.form['uebung']
        kilo = request.form['kilo']
        wiederholungen = request.form['wiederholungen']

        save(uebung, kilo, wiederholungen)
        return render_template('tracker1.html')
    return render_template('tracker1.html')

@app.route('/tracking', methods=['POST','GET'])
def liste():
    gespeicherten_eintraege= tracken()
    return render_template('tracking.html',
                           tracker=gespeicherten_eintraege)

@app.route('/tracking/<uebung>')
def einzel_liste(uebung):
    gespeicherten_eintraege = tracken()

    neue_liste = []
    for eintrag in gespeicherten_eintraege:
        if eintrag ['uebung'] == uebung:
            neue_liste.append(eintrag)
            return render_template('tracking.html', tracker=neue_liste)
@app.route('/analyse')
def analyse():
    gespeicherten_eintraege= tracken()
    analyse_ergebnis = summe_der_uebung(gespeicherten_eintraege)
    return render_template('analyse.html', tracker=analyse_ergebnis)

@app.route('/highscore')
def highscores():

    uebung_and_gewicht = get_scores()


    return render_template("highscore.html", page_title="Highscores", highscore=uebung_and_gewicht)










if __name__ == "__main__":
    app.run(debug=True, port=5000)
