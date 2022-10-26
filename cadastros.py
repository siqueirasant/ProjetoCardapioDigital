from this import d
from flask import Flask, request, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy


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

# 4. Função que alimenta a tabela produtos
class TbProdutos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_prod = db.Column(db.String, nullable = False)
    desc_prod = db.Column(db.String, nullable = False)
    qtd_prod = db.Column(db.String, nullable = False)
    print(f'Produto {nome_prod} cadastrado com sucesso!')


# 5. Função que alimenta a tabela de pedidos
class TbPedidos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_cliente = db.Column(db.String, nullable = False)
    desc_ped = db.Column(db.String, nullable = False)

