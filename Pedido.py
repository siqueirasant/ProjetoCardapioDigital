from main import db


# Classe que alimenta a tabela de pedidos
class TbPedidos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_cliente = db.Column(db.String, nullable = False)
    desc_ped = db.Column(db.String, nullable = False)
    preco_ped = db.Column(db.Numeric, nullable = False)

    def cadastra_pedido(nome, desc, preco):
        novoPedido = TbPedidos(
            nome_cliente = nome, 
            desc_ped = desc,
            preco_ped = preco
        )
        db.session.add(novoPedido)
        db.session.commit()

        return print("Pedido realizado com sucesso")

    def mostra_todos():
        return TbPedidos.query.all()
        
    def mostra_pedido(nome):
        return TbPedidos.query.filter_by(nome_cliente = nome).first()

    def atualiza_pedido(id, nome, desc,preco):
        pedido = TbPedidos.query.filter_by(id = id).first()
        pedido.nome_cliente = nome
        pedido.desc_ped = desc
        pedido.preco_ped = preco

        db.session.add(pedido)
        db.session.commit()
        return print("Pedido de " + pedido.nome_cliente + " atualizado com sucesso")

    # Função que deleta o cadastro do produto
    def deleta_pedido(id):
        TbPedidos.query.filter_by(id = id).delete()
        db.session.commit()
        return print("Pedido deletado com sucesso!")
