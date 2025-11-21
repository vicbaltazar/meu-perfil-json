from main import app
from flask import render_template

#Rotas
@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/blog')
def blog():
    return "Bem-vindo(a) ao Blog Jurássico!"

@app.route("/curiosidades")
def curiosidades():
    return render_template("curiosidades.html")

@app.route("/dinossauros")
def dinossauros():
    return render_template("dinossauros.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")