from flask import render_template, request, redirect, session, flash, url_for
from main import app, db
from Clientes import *

@app.route("/minhaConta.html")
def minha_conta():
    cliente = TbCadastro.mostra_todos()
    return render_template("minhaConta.html", cliente = cliente)


@app.route("/perfil.html")
def perfil():
    return render_template("perfil.html")

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
        return redirect("/")
    return render_template("cadastro.html")


@app.route("/editaCliente/<int:id>")
def edita_cliente(id):
    cliente = TbCadastro.mostra_cliente(id)
    return render_template("perfil.html", id=id)

@app.route("/atualizarCliente", methods=["POST"])
def atualizar_dados_cliente():
        id = request.form['id']
        nome = request.form['nome']
        logradouro = request.form['inputRua']
        nro = request.form['inputNumero']
        bairro = request.form['inputBairro']
        cidade = request.form['inputCidade']
        cep = request.form['inputCEP']
        telefone = request.form['inputTelefone']
        email = request.form['inputEmail']
        senha = request.form['inputSenha']
        TbCadastro.atualiza_cliente(id, nome, logradouro, nro, bairro, cidade,
        cep, telefone, email, senha)
        return redirect(url_for('minha_conta'))

@app.route("/deletarCliente/<int:id>")
def excluir_dados_cliente(id):
    TbCadastro.deleta_cliente(id)
    return redirect(url_for('cadastrar_cliente'))
