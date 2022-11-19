from main import db

class TbPedidos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_prod = db.Column(db.String, nullable = False)
    desc_prod = db.Column(db.String, nullable = False)
    preco_prod = db.Column(db.Numeric, nullable = False)
    qtd_prod = db.Column(db.Numeric, nullable = False)

    def cadastra_pedido(nome, desc, qtd, preco):
        novoPedido = TbPedidos(
            nome_prod = nome, 
            desc_prod = desc,
            qtd_prod = qtd,
            preco_prod = preco)
        db.session.add(novoPedido)
        db.session.commit()

        return print("Pedido realizado com sucesso")

    def mostra_todos():
        return TbPedidos.query.all()
        
    def mostra_pedido(id):
        return TbPedidos.query.filter_by(id = id).first()

    def atualiza_pedido(id, nome, desc, qtd, preco):
        pedido = TbPedidos.query.filter_by(id = id).first()
        pedido.nome_prod = nome
        pedido.desc_prod = desc
        pedido.qtd_prod = qtd
        pedido.preco_prod = preco

        db.session.add(pedido)
        db.session.commit()
        return print("Pedido de " + pedido.nome_prod  + " atualizado com sucesso")

    def deleta_pedido(id):
        TbPedidos.query.filter_by(id = id).delete()
        db.session.commit()
        return print("Pedido deletado com sucesso!")
