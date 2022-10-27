from cadastros import app, db


# Classe que alimenta a tabela de pedidos
class TbPedidos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_cliente = db.Column(db.String, nullable = False)
    desc_ped = db.Column(db.String, nullable = False)
    preco_ped = db.Colum(db.Numeric, nullable = False)

    # função de cadastro de pedido
    def cadastrar_pedido(self):
        with app.app_context():
            novoPedido = TbPedidos(
                nome_cliente = "", 
                desc_pedido = "")
        db.session.add(novoPedido)
        db.session.commit(self)

    # Função que consulta o pedido
    def consultar_pedido(self):
        pass

    # Função que exclui o pedido
    def excluir_pedido(self):
        pass

