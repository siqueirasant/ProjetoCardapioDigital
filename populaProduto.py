from listaProdutos import produtos
from Produtos import *


# Cadastrar todos os produtos da lista
def popula_produto():
    for i in produtos:
        try:
            nome = produtos[str(i)]["nome"]
            desc = produtos[str(i)]["descricao"]
            qtd = produtos[str(i)]["Quantidade"]
            preco = produtos[str(i)]["Preço"]
            TbProdutos.cadastrar_produto(nome,desc,qtd,preco)
            print(f'Produto {nome} cadastrado com sucesso')
        except Exception as e:
            print(e)

popula_produto()