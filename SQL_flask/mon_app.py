from flask import Flask, render_template, request, redirect, url_for
import pycountry
from wtforms.validators import DataRequired
from wtforms import validators
import re
import bleach.sanitizer
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sebroot",
    database="sqlform"
)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/merci", methods=["POST"])
def merci():
    return render_template("merci.html")

@app.route("/formulaires", methods=["GET", "POST"])
def formulaires():
    error_message = ""
    nom = ""
    prenom = ""
    email = ""
    pays = ""
    genre = ""
    sujet = ""
    commentaire = ""
    countries = [country.name for country in pycountry.countries]

    if request.method == "POST":

        cursor = db.cursor()

        create_table = """
            CREATE TABLE IF NOT EXISTS sqlform (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(255),
            prenom VARCHAR(255),
            email VARCHAR(255),
            pays VARCHAR(255),
            genre VARCHAR(255),
            sujet VARCHAR(255),
            commentaire VARCHAR(255)
            )
        """

        cursor.execute(create_table)
        db.commit()


        nom = bleach.clean(request.form.get('nom'))
        prenom = bleach.clean(request.form.get('prenom'))
        email = bleach.clean(request.form.get('email'))
        pays = bleach.clean(request.form.get('pays'))
        genre = bleach.clean(request.form.get('choix-genre'))
        sujet = bleach.clean(request.form.get('choix-sujet'))
        commentaire = bleach.clean(request.form.get('commentaire'))

        my_query = """INSERT INTO sqlform (nom, prenom, email, pays, genre, sujet, commentaire)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(my_query, (nom, prenom, email, pays, genre, sujet, commentaire))
        db.commit()

        if not (nom.isalpha() and prenom.isalpha() and re.match(r"[^@]+@[^@]+\.[^@]+", email)):

            if not nom.isalpha():
                nom = ""
                error_message = 'Nom et Prénom doivent être alphanumériques, et l adresse email doit être valide. Vérifiez vos inputs.'
            if not prenom.isalpha():
                prenom = ""
                error_message = 'Nom et Prénom doivent être alphanumériques, et l adresse email doit être valide. Vérifiez vos inputs.'
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                email = ""
                error_message = 'Nom et Prénom doivent être alphanumériques, et l adresse email doit être valide. Vérifiez vos inputs.'

    if nom == '' or prenom == '' or email == '':
        return render_template('formulaires.html', nom=nom, prenom=prenom, email=email, countries=countries, pays=pays, genre=genre, sujet=sujet, commentaire=commentaire, error=error_message)
    else:
        return render_template('merci.html', nom=nom, prenom=prenom, email=email, countries=countries, pays=pays, genre=genre, sujet=sujet, commentaire=commentaire)


if __name__ == '__main__':
    app.run(debug=True)

