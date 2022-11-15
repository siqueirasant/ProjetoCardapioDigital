from main import db


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


    def mostra_todos():
        return TbProdutos.query.all()

    def mostra_produto(nome):
        return TbProdutos.query.filter_by(nome_prod = nome).first()

    def atualiza_produto(id, nome, desc, qtd, preco):
        produto = TbProdutos.query.filter_by(id = id).first()
        produto.nome_prod = nome
        produto.desc_prod = desc
        produto.qtd_prod = qtd
        produto.preco_prod = preco

        db.session.add(produto)
        db.session.commit()
        return print("Produto " + produto.nome_prod + " atualizado com sucesso")

    # Função que deleta o cadastro do produto
    def deleta_produto(id):
        TbProdutos.query.filter_by(id = id).delete()
        db.session.commit()
        return print("Produto deletado com sucesso!")
