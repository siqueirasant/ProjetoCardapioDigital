from cadastros import TbPedidos, app, db, TbProdutos, TbPedidos

#conectando banco
#Banco().iniciaBanco()

#Função de cadastro dos produtos para alimentar o banco de dados

with app.app_context():
    novoProduto = TbProdutos(
        nome_prod = "Bolo de Chocolate", 
        desc_prod = "Bolo de chocolate com duas camadas de recheio de ganache de chocolate ao leite, com cobertura de chantilly.",
        qtd_prod = 5)
    db.session.add(novoProduto)
    db.session.commit()

# função de cadastro de pedido
with app.app_context():
    novoPedido = TbPedidos(
        nome_cliente = "", 
        desc_pedido = "")
    db.session.add(novoPedido)
    db.session.commit()