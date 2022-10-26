from funcoes_uteis import Funcoes
from Banco import Banco

from flask import Flask, request, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy

funcoes = Funcoes()


app = Flask(__name__)

app.secret_key = 'blablabla'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/cardapio'
db = SQLAlchemy(app)

class TbCadastro (db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    nome = db.Column(db.String, nullable = False)
    logradouro = db.Column(db.String, nullable = False)
    nro = db.Column(db.Integer, nullable = False)
    bairro = db.Column(db.String, nullable = False)
    cidade = db.Column(db.String, nullable = False)
    cep = db.Column(db.String, nullable = False)
    telefone = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)
    senha = db.Column(db.String, nullable = False)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sobre.html")
def sobre():
    return render_template("sobre.html")


@app.route("/contato.html")
def contato():
    return render_template("contato.html")


@app.route("/encomenda.html")
def encomenda():
    return render_template("encomenda.html")


@app.route("/cadastro.html", methods=["GET", "POST"])
def cadastrar_cliente():
    if request.method == "POST":

        nome = request.form['inputNome']
        logradouro = request.form['inputRua']
        nro = request.form['inputNumero']
        bairro = request.form['inputBairro']
        cidade = request.form['inputCidade']
        cep = request.form['inputCEP']
        telefone = request.form['inputTelefone']
        email = request.form['inputEmail']
        senha = request.form['inputSenha']

        cadastro = TbCadastro.query.filter_by(email = email).first()
        if cadastro:
            flash('Usuario já cadastrado')
            return render_template("cadastro.html")
   
        novoCadastro = TbCadastro(nome = nome, logradouro = logradouro,
        nro = nro, bairro = bairro, cidade = cidade, cep = cep, 
        telefone = telefone, email = email, senha = senha)
        db.session.add(novoCadastro)
        db.session.commit()
        flash("Cadastro realizado com sucesso!")
        return render_template("cadastro.html")

    return render_template("cadastro.html")



@app.route("/login.html", methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@app.route("/autenticar", methods=['POST'])
def autenticar ():
    email = request.form['inputEmail']
    senha = request.form['inputSenha']
    usuario = TbCadastro.query.filter_by(senha = senha, email = email).first()
    db.session.commit()
    if usuario:
        flash("Login realizado com sucesso")
        return redirect("/login.html")
    
    flash("Senha ou email incorretos")
    return redirect("/login.html")
    
"""
@app.route("/atualizar", methods=["PUT"])
def atualizar_dados_cliente():
    pass


@app.rout("/exibirPedido", methods=["GET"])
def exibir_dados_pedido():
    pass
"""

app.run(debug=True)
