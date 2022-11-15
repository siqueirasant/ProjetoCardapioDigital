from flask import render_template, request, redirect, session, flash, url_for
from main import app, db
from Clientes import TbCadastro

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sobre.html")
def sobre():
    return render_template("sobre.html")

@app.route("/perfil.html")
def perfil():
    return render_template("perfil.html")

@app.route("/carrinhoPage.html")
def carrinho():
    return render_template("carrinhoPage.html")

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

        with app.app_context():
            cadastro = TbCadastro.query.filter_by(email = email).first()
        if cadastro:
            flash('Usuario já cadastrado')
            return render_template("cadastro.html")

        with app.app_context():
            TbCadastro.cadastra_cliente(nome, logradouro, nro, bairro, cidade, cep, telefone, email, senha)
            cliente = TbCadastro.mostra_clientes(nome)
            print(cliente)
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
