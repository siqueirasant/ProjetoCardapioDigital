from funcoes_uteis import Funcoes

from flask import Flask, request, render_template

funcoes = Funcoes()


app = Flask(__name__)


@app.route("/index.html")
def home():
    return render_template("index.html")


@app.route("/sobre.html")
def sobre():
    return render_template("sobre.html")


@app.route("/contato.html")
def contato():
    return render_template("contato.html")


@app.route("/encomenda.html")
def encomenda():
    return render_template("encomenda.html")


@app.route("/cadastro.html", methods=["GET", "POST"])
def cadastrar_cliente():
    if request.method == "POST":
        id = 1
        nome = request.form['inputNome']
        logradouro = request.form['inputRua']
        nro = request.form['inputNumero']
        bairro = request.form['bairroHelp']
        cidade = request.form['cidadeHelp']
        cep = request.form['inputCEP']
        telefone = request.form['inputTelefone']
        email = request.form['inputEmail']
        senha = request.form['inputSenha']
        print(
            id,
            nome,
            logradouro,
            nro,
            bairro,
            cidade,
            cep,
            telefone,
            email,
            senha
            )
        return render_template("cadastro.html")
    else:
        return render_template("cadastro.html")


@app.route("/login.html", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        usuario = request.form['inputEmail']
        senha = request.form['inputSenha']
        print(usuario, senha)
        return render_template("login.html")
    else:
        return render_template("login.html")


"""
@app.route("/atualizar", methods=["PUT"])
def atualizar_dados_cliente():
    pass


@app.rout("/exibirPedido", methods=["GET"])
def exibir_dados_pedido():
    pass
"""

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
