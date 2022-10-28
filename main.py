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