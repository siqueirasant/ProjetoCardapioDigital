import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='root'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `cardapio`;")

cursor.execute("CREATE DATABASE `cardapio`;")

cursor.execute("USE `cardapio`;")

# criando tabelas
TABLES = {}
TABLES['tb_cadastro'] = ('''
      CREATE TABLE `tb_cadastro` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `logradouro` varchar(40) NOT NULL,
      `nro` int(30) NOT NULL,
      `bairro` varchar(30) NOT NULL,
      `cidade` varchar(30) NOT NULL,
      `cep` varchar(30) NOT NULL,
      `telefone` varchar(30) NOT NULL,
      `email` varchar(30) NOT NULL,
      `senha` varchar(30) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Login'] = ('''
      CREATE TABLE `login` (
      `email` varchar(20) NOT NULL,
      `senha` varchar(100) NOT NULL,
      PRIMARY KEY (`email`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()