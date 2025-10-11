import mysql.connector # importa a biblioteca

def conexao_banco(): # criando uma função de conexão com o banco
    conexao = mysql.connector.connect(
        host = 'localhost'            # endereço do banco de dados
        user =  'root'            # usuário do banco de dados
        password = ''         # senha do banco de dados
        database = 'aula'         # nome do banco de dados


    )