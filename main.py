# Importar
from flask import Flask, render_template, redirect, request, url_for, session
from flask_sqlalchemy import SQLAlchemy
from random import choice
import requests
import time
import urllib
from speech import speech
from game import *


app = Flask(__name__)
app.secret_key = "supersecretkey"
nivel = 1

# La primera página
@app.route('/')
def index():
    session['score'] = session.get('score', 0)
    return render_template('inicio.html', word=None, score=session['score'], spoken_word=None, error=None, recognizing=False)


@app.route('/<size>')
def lights(size):
    global nivel
    print(size)
    return render_template(f'nivel{nivel}.html',size=size)


@app.route('/voice', methods=["POST"])
def voices():
    global nivel
    try:
        correct_word = request.form["correct_word"]
        text= speech()
        num = compara(correct_word, text)
        error= None

        if num==1:
            session["score"]+=1
        elif num==2:
            session["score"]+=2

    except:
        text= "No comprendí"
    return render_template(f"nivel{nivel}.html",word=None, score=session['score'], spoken_word=text, error=error, recognizing=False)

@app.route('/mostrar', methods=["POST"])
def mostrar():
    global nivel
    word = play_game(nivel)
    return render_template(f"nivel{nivel}.html", word=word, score=session['score'], spoken_word=None, error=None, recognizing=False)


@app.route('/recognize', methods=['POST'])
def recognize():
    global nivel
    correct_word = request.form['correct_word']
    return render_template(f'nivel{nivel}.html', word=correct_word, score=session['score'], spoken_word=None, error=None, recognizing=True)

app.run(debug=True)
