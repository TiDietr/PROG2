from flask import Flask
from flask import render_template
from flask import request

from daten import speichern

app = Flask("Fitnessplan!")


@app.route('/')
def start():
    titel_text = 'Wilkommen beim persönlichen Fitnessplan'
    einleitungs_text = 'Hier können sie Ihren Fitnessplan erstellen'
    return render_template('start.html', app_name='Fitnessplan!', ueberschrift=titel_text, einleitung=einleitungs_text)

@app.route('/eingabe', methods=['POST','GET'])
def eingabe():
    if request.method =='POST':
        aktivitaet = request.form['aktivitaet']
        gewicht = request.form['gewicht']
        wiederholung = request.form['wiederholung']
        antwort = speichern(aktivitaet, gewicht, wiederholung)
        return 'Erfolgreiche Eingabe: <br>'+ str(antwort)
    return render_template('eingabe.html', app_name='Fitnessplan! - Eingabe')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
