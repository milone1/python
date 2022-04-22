import re
from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    ##return '<center><h1>Bienvenidos a mi sitio web</h1></center>'
    listaPeliculas = ['CODA','SONIC2','SPIDERMAN']
    nombre = request.args.get('nombre','no hay nombre')
    context = {
        'nombre':nombre
    }
    return render_template('index.html',**context)

@app.route('/peliculas')
def peliculas():
    listaPeliculas = ['CODA','SPIDER-MAN','IRON-MAN']
    nombre = request.args.get('nombre','')
    context = {
        'nombre':nombre,
        'peliculas':listaPeliculas
    }
    return render_template('peliculas.html',**context)


app.run(debug = True)