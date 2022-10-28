from logging import PercentStyle
from main import app, db


# Classe que alimenta a tabela produtos
class TbProdutos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_prod = db.Column(db.String, nullable = False)
    desc_prod = db.Column(db.String, nullable = False)
    preco_prod = db.Column(db.Numeric, nullable = False)
    qtd_prod = db.Column(db.String, nullable = False)

    #Função de cadastro dos produtos para alimentar o banco de dados
    def cadastrar_produto(nome, desc, qtd, preco):
        produto = TbProdutos(
            nome_prod = nome, 
            desc_prod = desc,
            qtd_prod = qtd,
            preco_prod = preco)
        db.session.add(produto)
        db.session.commit()


    # Função que consulta os produtos
    def consultar_produto(self):
        pass

    # Função que altera o cadastro do produto
    def alterar_produto(self):
        pass

    # Função que deleta o cadastro do produto
    def excluir_produto(self):
        pass
