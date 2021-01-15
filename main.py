from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from daten import speichern, laden
from index import status
from tracker import speichern1
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




#@app.route('/eingabe', methods=['POST', 'GET'])
#def eingabe_formular():
 #       if request.method == 'POST':
  #          aktivitaet = request.form['aktivitaet']
   #         gewicht = request.form['gewicht']
    #        wiederholung = request.form['wiederholung']
     #       kategorie = request.form['kategorie']
      #      antwort = speichern(aktivitaet, gewicht, wiederholung)
       #     return 'Erfolgreiche Eingabe: <br>' + str(antwort)

        #return render_template('eingabe.html', app_name='Fitnesscoach! - Eingabe', kategorien=farben.keys)



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
        datum= request.form.get('datum')

       # send_mail(

        #)
        return render_template('bestaetigung.html' , zeil=ziel, name = name, telefon=telefon, alter=alter,gewicht=gewicht,groesse=groesse, zeit=zeit, datum=datum)
    else:
        return render_template('fehler.html')




@app.route('/liste/<termine>')
def einzel_liste(termin):
    gespeicherten_eintraege = laden()
    neue_liste =[]
    for eintrag in gespeicherten_eintraege:
        if eintrag [0] == termin:
            neue_liste.append(eintrag)
    titel_text = 'Liste der Termine:' + termin
    einleitungs_text = 'Hier sind alle deine' +Termine +'Termine'
    return render_template(
        'liste.html',
        app_name='Fitnessplan!',
        ueberschrift=titel_text,
        einleitung=einleitungs_text,
        daten=neue_liste)




@app.route('/analyse')
def analyse():
    gespeicherten_eintraege = laden()
    analyse_ergebnis = summe_der_aktivitaeten(gespeicherten_eintraege)
    titel_text = 'Analyse deiner Aktivitaeten'
    einleitungs_text = 'Hier werden alle deine Aktivitaeten zusammengefasst angezeigt '
    return render_template(
        'analyse.html',
        app_name='Fitnessplan!',
        ueberschrift=titel_text,
        einleitung=einleitungs_text,
        daten=analyse_ergebnis
    )

@app.route('/tracker', methods=['POST','GET'])
def tracker():
    if request.method == 'POST':
        uebung = request.form['uebung']
        gewicht = request.form['gewicht']
        wiederholungen = request.form['wiederholungen']

        speichern1(uebung,gewicht, wiederholungen)
        return redirect('/fortschritt')
    return render_template('tracker.html')

@app.route('/liste')
def liste():
    gespeicherten_eintraege = laden()
    ueberschrifts_text = 'Liste deiner Aktivitäten'
    einleitung_text = 'Hier werden alle deine Aktivitäten die du aufgezeichnet hast angezeigt.'
    return render_template(
        'liste.html',
        app_name="Tracker!",
        ueberschrift=ueberschrifts_text,
        einleitung=einleitung_text,
        daten=gespeicherten_eintraege,
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)
