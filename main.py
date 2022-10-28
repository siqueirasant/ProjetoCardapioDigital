from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'blablabla'


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/cardapio'
db = SQLAlchemy(app)

from views import *
if __name__ == '__main__':
    app.run(debug=True)

""" from Clientes import TbCadastro
TbCadastro.cadastra_cliente(
    "Teste", "Teste", 38, "teste" , "cidade", "cep",
    "telefone", "email", "senha"
) """

#cliente = TbCadastro.mostra_clientes("Teste")
#print("Retornando cliente " + cliente.nome + " " + cliente.logradouro)
#TbCadastro.atualiza_cliente(1, "mudando", "mudando", 78, "mudando","mudando", "mudando", "mudando", "mudando", "mudando")
#TbCadastro.deleta_cliente(1)

""" from Produtos import TbProdutos
produto = TbProdutos.mostra_todos()
print(produto[0].nome_prod)
print(TbProdutos.mostra_produto("kit_festa_5").desc_prod)
TbProdutos.atualiza_produto(4, "mudando", "mudando", 1, 50.00)
TbProdutos.deleta_produto(3) """

""" from Pedido import TbPedidos
TbPedidos.cadastra_pedido(
    "Carla",
    "pedido tal",
    50.00   
)

print(TbPedidos.mostra_todos()[0].desc_ped)
print(TbPedidos.mostra_pedido("Carla").preco_ped)
TbPedidos.atualiza_pedido(1, "Cristina", "teste mudança", 20)
TbPedidos.deleta_pedido(2) """



