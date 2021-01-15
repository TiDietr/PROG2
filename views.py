def bestaetigung(request):
    if request.method == "POST":
        ziel = request.POSt['ziel']
        name = request.POST['name']
        telefon = request.POST['telefon']
        alter = request.POST['alter']
        gewicht = request.POST['gewicht']
        groesse = request.POST['groesse']
        zeit = request.POST['zeit']
        datum = request.POST['datum']

        return render_templates(request, 'bestaetigung.html', {
      'ziel': ziel,
            'name': name,
            'telefon': telefon,
            'alter': alter,
            'gewicht': gewicht,
            'groesse': groesse,
            'zeit': zeit,
            'datum': datum,
        })
    else:
        render_template (request, 'fehler.html',{})