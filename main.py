from flask import Flask
from flask import render_template
from flask import request, url_for
from flask import redirect
from flask import session


from termin import speichern, laden
from index import status, bmiladen, bmispeichern
from tracker import save, tracken
from berechnungen import summe_der_uebung

#Das Wissen wurden vom Youtube Kanal 'codemy.com', https://www.youtube.com/channel/UCFB0dxMudkws1q8w5NJEAmw, Stackoverflow.com, Vorlesung gewonnen.







app = Flask("Fitnesscoach!")
app.config['SESSION_TYPE'] = 'memcached' #Vergesslichkeit des Logins (jede Eingabe funktioniert)
app.config['SECRET_KEY'] = 'super secret key' #Secret_key für login für Verschlüsselung von Nachrichten. (teife Sicherheit)



@app.route('/')
def start():
    titel_text = 'Wilkommen beim persönlichen Fitnesscoach'
    einleitungs_text = 'Hier finden Sie alles zum Thema Fitness'
    return render_template('index.html', app_name='Fitnesscoach', ueberschrift=titel_text, einleitung=einleitungs_text)


@app.route('/termin', methods=['POST','GET'])
def eingabe_formular(): #Bildung der Funktion
    if request.method == 'POST': # Die Post Methode dient dazu, die Daten auf den Server zu laden.
        ziel = request.form['ziel'] # Hier werden die eingegebenen Daten aus Form gespeichert.
        name = request.form['name']
        telefon = request.form['telefon']
        alter = request.form['alter']
        gewicht = request.form['gewicht']
        groesse = request.form['groesse']
        zeit = request.form['zeit']
        daten = request.form['daten']

        speichern(name, ziel,telefon,alter,groesse,gewicht, zeit,daten) # Daten in json speichern
        return redirect('/bestaetigung')
    return render_template('termin.html')

@app.route('/bmi', methods=['POST','GET'])
def rechner(): #Bildung der Funktion
    bmi=''
    berechnung=''
    if request.method == 'POST' and 'gewicht' in request.form and 'groesse' in request.form:#Post Daten auf Server laden und auf request.form
        gewicht=float(request.form.get('gewicht'))
        groesse=float(request.form.get('groesse'))
        bmi = round(gewicht/(groesse * groesse),2)
        berechnung=status(bmi)
        #bmispeichern(bmi)

    return render_template("bmi.html", bmi=bmi, berechnung=berechnung)



@app.route('/bestaetigung', methods=['POST','GET'])
def bestaetigung(): #Bildung der Funktion
    if request.method == 'POST' and 'ziel' in request.form and 'name' in request.form and 'telefon' in request.form and 'alter' in request.form and 'gewicht' in request.form and 'groesse' in request.form and 'zeit' in request.form and 'daten' in request.form: #Post Daten auf Server laden und auf request.form
        ziel = request.form.get('ziel') #Daten von Formular zurückgeben
        name = request.form.get('name')
        telefon= request.form.get('telefon')
        alter= request.form.get('alter')
        gewicht= request.form.get('gewicht')
        groesse= request.form.get('groesse')
        zeit= request.form.get('zeit')
        daten= request.form.get('daten')


        speichern(name, ziel,telefon,alter,groesse,gewicht, zeit, daten)
        return render_template('bestaetigung.html' , ziel=ziel, name = name, telefon=telefon, alter=alter,gewicht=gewicht,groesse=groesse, zeit=zeit, daten=daten)
    else:
        return render_template('fehler.html')







@app.route('/tracker', methods=['POST','GET'])
def tracker(): #Bildung der Funktion
    if request.method == 'POST':
        uebung = request.form['uebung']
        gewicht = request.form['kilo']
        wiederholungen = request.form['wiederholungen']

        save(uebung,gewicht, wiederholungen)
        return render_template('tracker1.html')
    return render_template('tracker.html')

@app.route('/trackermore', methods=['POST','GET'])
def tracker1(): #Bildung der Funktion
    if request.method == 'POST':
        uebung = request.form['uebung']
        kilo = request.form['kilo']
        wiederholungen = request.form['wiederholungen']

        save(uebung, kilo, wiederholungen)
        return render_template('tracker1.html')
    return render_template('tracker1.html')

@app.route('/tracking', methods=['POST','GET'])
def liste(): #Bildung der Funktion
    gespeicherten_eintraege= tracken()
    return render_template('tracking.html',
                           tracker=gespeicherten_eintraege)

@app.route('/tracking/<uebung>')
def einzel_liste(uebung): #Bildung der Funktion für  uebung
    gespeicherten_eintraege = tracken()
    neue_liste = ['uebung']
    for eintrag in gespeicherten_eintraege:
        if eintrag ['uebung'] == uebung:
            neue_liste.append(eintrag)
            return render_template('tracking.html', tracker=neue_liste)




@app.route('/terminliste', methods=['POST','GET'])
def terminliste(): #Bildung der Funktion
    gespeicherten_eintraege= laden()
    return render_template('terminliste.html',
                           termin=gespeicherten_eintraege)

@app.route('/terminliste/<name>')
def einzel_liste2(name): #Bildung der Funktion für name
    gespeicherten_eintraege = laden()

    neue_liste2 = []
    for eintrag in gespeicherten_eintraege:
        if eintrag['name'] == name:
            neue_liste2.append(eintrag)
            return render_template('terminliste.html', termin=neue_liste2)


@app.route('/login', methods=['GET', 'POST'])
def login(): #Bildung der Funktion
    if request.method == 'POST':
        session.pop('user', None) #kein Vorgegebener User für das Login

        if request.form['password'] == 'password':
            session['user'] = request.form['username']
            return redirect(url_for('terminliste')) #nach Eingabe direkte Weiterleitung zu terminliste.html

    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
