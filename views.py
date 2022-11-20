from flask import render_template, request, redirect, session, flash, url_for
from main import app, db
from Clientes import TbCadastro

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sobre.html")
def sobre():
    return render_template("sobre.html")


@app.route("/contato.html")
def contato():
    return render_template("contato.html")

@app.route("/login.html", methods=['GET','POST'])
def autenticar():
    if request.method == "POST":
        email = request.form['inputEmail']
        senha = request.form['inputSenha']
        with app.app_context():
            usuario = TbCadastro.autentica_cliente(email, senha)
        if usuario:
            #flash("Login realizado com sucesso!")
            return redirect("encomenda.html")
        flash("Senha ou email incorretos.")
        return redirect("/login.html")
    return render_template("login.html")    



