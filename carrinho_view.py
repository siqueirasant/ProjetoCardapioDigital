from flask import render_template, request, redirect, session, flash, url_for
from main import app, db
from Pedido import *
from Produtos import *

@app.route('/encomenda.html')
def encomenda():
    produtos = TbProdutos.mostra_todos()
    return render_template("encomenda.html", produtos = produtos)

@app.route('/carrinhoPage.html')
def carrinho_page():
    pedidos = TbPedidos.mostra_todos()
    return render_template('carrinhoPage.html', pedidos=pedidos)

@app.route('/carrinho.html')
def carrinho():
    pedidos = TbPedidos.mostra_todos()
    total = mostrar_total()
    return render_template("carrinho.html", pedidos = pedidos, total = total)

@app.route('/cadastraPedido/<int:id>')
def cadastra_pedido(id):
    produto = TbProdutos.mostra_produto(id=id)
    return render_template('cadastraPedido.html', produto = produto, id=id)

@app.route('/adicionaCarrinho', methods=['POST'])
def adiciona_carrinho():
    id = request.form['id']
    produto = TbProdutos.mostra_produto(id=id)
    nome = produto.nome_prod
    desc = produto.desc_prod
    qtd = request.form['quantidade']
    precoUnidade = produto.preco_prod
    precoTotal = precoUnidade * float(qtd)
    TbPedidos.cadastra_pedido(nome, desc, qtd, precoTotal)
    return redirect(url_for('carrinho'))

@app.route('/editarCarrinho/<int:id>')
def editar_carrinho(id):
    pedido = TbPedidos.mostra_pedido(id=id)
    return render_template("editarCarrinho.html", pedido = pedido , id=id)

@app.route('/atualizarCarrinho', methods=['POST'])
def atualizar_carrinho():
    id = request.form['id']
    pedido = TbPedidos.mostra_pedido(id)
    quantidade = request.form['quantidade']
    nome = pedido.nome_prod
    desc = pedido.desc_prod
    preco = pedido.preco_prod
    TbPedidos.atualiza_pedido(id, nome, desc, quantidade,preco)
    return redirect(url_for('carrinho'))

@app.route('/deletarCarrinho/<int:id>')
def deleta_carrinho(id):
    TbPedidos.deleta_pedido(id)
    return redirect(url_for('carrinho'))

def mostrar_total():
    pedidos = TbPedidos.mostra_todos()
    total = 0
    for pedido in pedidos:
        total = total + pedido.preco_prod
    return total

@app.route("/resumoPedido.html")
def resumo_pedido():
    pedidos = TbPedidos.mostra_todos()
    total = mostrar_total()
    return render_template("resumoPedido.html", total = total, pedidos = pedidos)
    