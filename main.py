from flask import Flask
from flask import render_template
from flask import request

from daten import speichern, laden
from berechnungen import summe_der_aktivitaeten



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

@app.route('/bmi')
def bmi():
    titel_text = 'Wilkommen beim persönlichen Fitnesscoach'
    einleitungs_text = 'Hier finden Sie alles zum Thema Fitness'
    return render_template('bmi.html', app_name='Fitnesscoach', ueberschrift=titel_text, einleitung=einleitungs_text)

@app.route('/tracker')
def tracker():
    titel_text = 'Wilkommen beim persönlichen Fitnesscoach'
    einleitungs_text = 'Hier finden Sie alles zum Thema Fitness'
    return render_template('tracker.html', app_name='Fitnesscoach', ueberschrift=titel_text, einleitung=einleitungs_text)

@app.route('/termin')
def termin():
    titel_text = 'Wilkommen beim persönlichen Fitnesscoach'
    einleitungs_text = 'Hier finden Sie alles zum Thema Fitness'
    return render_template('termin.html', app_name='Fitnesscoach', ueberschrift=titel_text, einleitung=einleitungs_text)



@app.route('/eingabe', methods=['POST','GET'])
def eingabe_formular():
    if request.method =='POST':
        aktivitaet = request.form['aktivitaet']
        gewicht = request.form['gewicht']
        wiederholung = request.form['wiederholung']
        kategorie = request.form['kategorie']
        antwort = speichern(aktivitaet, gewicht, wiederholung, kategorie)
        return 'Erfolgreiche Eingabe: <br>'+ str(antwort)

    return render_template('eingabe.html', app_name='Fitnesscoach! - Eingabe', kategorien=farben.keys())

@app.route('/liste')
def liste():
    gespeicherten_eintraege = laden()
    titel_text = 'Liste deiner Aktivitaeten'
    einleitungs_text = 'Hier werden alle deine Aktivitaeten angezeigt '
    return render_template(
        'liste.html',
        app_name='Fitnessplan!',
        ueberschrift=titel_text,
        einleitung=einleitungs_text,
        daten=gespeicherten_eintraege,
        farben_dict=farben
    )

@app.route('/liste/<aktivitaet>')
def einzel_liste(aktivitaet):
    gespeicherten_eintraege = laden()
    neue_liste =[]
    for eintrag in gespeicherten_eintraege:
        if eintrag [0] == aktivitaet:
            neue_liste.append(eintrag)
    titel_text = 'Liste deiner Aktivitaeten:' + aktivitaet
    einleitungs_text = 'Hier sind alle deine' +aktivitaet +'Aktivitaeten'
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


if __name__ == "__main__":
    app.run(debug=True, port=5000)
