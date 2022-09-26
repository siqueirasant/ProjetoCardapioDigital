# ProjetoCardapioDigital
Projeto ADS EAD Cardápio Digital


Banco de dados- MYSQL

PARA RODAR O BANCO LOCALMENTE:

    - Abra o cmd e execute o seguinte comando: pip3.exe install mysqlclient
    (será necessário, se não tiver o mysqsl instalado, configurar o host, user e password.
    Nesse caso, o password e user usando no projeto é 'root', caso queira escolher outro de sua
    preferência, será necessário setar essas informações no set up do banco aqui na aplicação).

    - baixe também o conector do mysql com o seguinte comando: pip install mysql-connector-python==8.0.28

    - baixe também o SQLAlchemy, ele será necessário para traduzir um objeto python para um objeto de banco de dados, tornando a persistência possível. Execute o seguinte comando:  pip install flask -sqlalchemy==2.5.1

    - Após essas configurações, rode somente o arquivo setup_banco.py (ele criará o database e as tabelas necessárias para utilização da aplicação. TODO: tornar esse script parte da aplicação, assim não será necessário rodar separado).
