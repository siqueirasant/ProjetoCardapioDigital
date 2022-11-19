from flask import render_template, request, redirect, session, flash, url_for
from main import app, db
from Produtos import *


@app.route("/produtos.html")
def produtos():
    produtos = TbProdutos.mostra_todos()
    return render_template("produtos.html", produtos = produtos)

@app.route('/editar/<int:id>')
def editar(id):
    produto = TbProdutos.mostra_produto(id=id)
    print(produto.nome_prod)
    return render_template("editar.html", id=id)  

@app.route('/atualizar', methods=['POST'])
def atualizar():
    id = request.form['id']
    nome = request.form['nome']
    descricao = request.form['descricao']
    quantidade = request.form['quantidade']
    preco = request.form['preco']
    TbProdutos.atualiza_produto(id, nome, descricao, quantidade, preco)
    return redirect(url_for('produtos'))

@app.route('/deletar/<int:id>')
def deletar(id):
    TbProdutos.deleta_produto(id)
    return redirect(url_for('produtos'))  
