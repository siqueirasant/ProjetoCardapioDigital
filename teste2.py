
#conectando banco
"""
from Banco import *
Banco().iniciaBanco()
"""

# Produtos
from listaProdutos import produtos
from produtos import *
p = TbProdutos()

# Consultar produto
with app.app_context():
    produtos = TbProdutos()
    qtd = produtos.cadastrar_produto.query.all()
    print(qtd)

"""
# Cadastrar todos os produtos da lista
for i in produtos:
    try:
        produto = i
        desc = produtos[str(i)]["descricao"]
        qtd = produtos[str(i)]["Quantidade"]
        preco = produtos[str(i)]["Preço"]
        with app.app_context():
            p.cadastrar_produto(
                nome = produto,
                desc = desc,
                qtd = qtd,
                preco = preco
            )
            print(f'Produto {produto} cadastrado com sucesso')
    except Exception as e:
        print(e)
"""