from flask_sqlalchemy import SQLAlchemy
from main import db


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



    def cadastra_cliente(nome, logradouro, nro, bairro, cidade, cep, telefone, email, senha):
        novo_cliente = TbCadastro(
            nome = nome, logradouro = logradouro,
            nro = nro, bairro = bairro, cidade = cidade,
            cep = cep, telefone = telefone, email = email,
            senha = senha)
        db.session.add(novo_cliente)
        db.session.commit()
        print("Cadastro realizado com sucesso")
    
    def mostra_clientes(nome):
        cliente = TbCadastro.query.filter_by(nome = nome).first()
        return cliente
    
    def atualiza_cliente (id, nome, logradouro, nro, bairro, cidade, cep, telefone, email, senha):
        cliente = TbCadastro.query.filter_by(id = id).first()
        cliente.nome = nome
        cliente.logradouro = logradouro
        cliente.nro = nro
        cliente.bairro = bairro
        cliente.cidade = cidade
        cliente.cep = cep
        cliente.telefone = telefone
        cliente.email = email
        cliente.senha = senha
        db.session.add(cliente)
        db.session.commit()
        return print("Atualização de cadastro de realizado com sucesso")


    def deleta_cliente(id):
        TbCadastro.query.filter_by(id=id).delete()
        db.session.commit()
        return print("Cadastro deletado com sucesso")

