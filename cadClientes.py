from funcoes_uteis import FuncoesUteis

from dataclasses import dataclass
from flask import Flask, request, render_template


@dataclass
class CadastroCliente():
    app = Flask(__name__)
    funcoes = FuncoesUteis()

    @app.route("/cadastro", methods=["POST"])
    def cadastrar_cliente(self):
        id = self.funcoes.calcular_id_cliente()
        nome = request.form['nome']
        logradouro = request.form['logradouro']
        nro = request.form['nro']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        cep = request.form['cep']
        telefone = request.form['telefone']
        email = request.form['email']
        print(id, nome, logradouro, nro, bairro, cidade, cep, telefone, email)
        return render_template("cadastro.html")

    @app.route("/atualizar", method=["PUT"])
    def atualizar_dados_cliente(self):
        pass

    @app.rout("/exibirPedido", methods=["GET"])
    def exibir_dados_pedido(self):
        pass
