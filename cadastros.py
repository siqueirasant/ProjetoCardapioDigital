from this import d
<<<<<<< HEAD
from flask import Flask
=======
from flask import Flask, request, render_template, flash, redirect
>>>>>>> a384cfd6123f5085bcfca0569341f3386db8ba31
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

<<<<<<< HEAD
    # Função que cadastra os dados do cliente
    def cadastrar(self, nome, logradouro, nro, bairro, cidade, cep, telefone, email, senha):
        with app.app_context():
            novoCadastro = TbCadastro(nome = nome, logradouro = logradouro,
            nro = nro, bairro = bairro, cidade = cidade, cep = cep, 
            telefone = telefone, email = email, senha = senha)
        db.session.add(novoCadastro)
        db.session.commit()

    # Função que consulta os dados do cliente
    def consultar_cadastro(self):
        pass


    # Função que altera o cadastro do cliente
    def alterar_cadastro(self):
        pass


    # Função que exclui cadastro de cliente
    def  excluir_cadastro(self):
        pass
=======
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

>>>>>>> a384cfd6123f5085bcfca0569341f3386db8ba31
