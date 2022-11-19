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


@app.route("/contato.html")
def contato():
    return render_template("contato.html")

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
            cadastro = TbCadastro.mostra_cliente(email=email)
        if cadastro:
            flash('Usuario já cadastrado!')
            return render_template("cadastro.html")

        with app.app_context():
            TbCadastro.cadastra_cliente(nome, logradouro, nro, bairro, cidade, cep, telefone, email, senha)
            cliente = TbCadastro.mostra_cliente(email)
            print(cliente)
        #flash("Cadastro realizado com sucesso!")
        return render_template("encomenda.html")
    return render_template("cadastro.html")


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


@app.route("/perfil.html", methods=["GET","POST"])
def atualizar_dados_cliente():
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
        
        consulta = TbCadastro.mostra_cliente(email=email)
        if consulta:
            with app.app_context():
                cliente = TbCadastro.atualiza_cliente(nome, logradouro, nro, bairro, cidade, cep, telefone, email, senha)
                print(f'cliente: {cliente}')
            flash("Cadastro alterado com sucesso!")
            return redirect("atualizar.html")
        else:
            flash("Cadastro não encontrado.")
            return redirect("perfil.html")
    return render_template("perfil.html")

@app.route("/deletar.html", methods=["GET", "POST"])
def excluir_dados_cliente():
    if request.method == "POST":
        email = request.form['inputEmail']
        with app.app_context():
            cad = TbCadastro.deleta_cliente(email)
        if cad == 0:
            flash("Cadastro não encontrado.")
        else:
            flash("Cadastro excluído com sucesso.")
        return redirect("deletar.html")
    return render_template("deletar.html")

