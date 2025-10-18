from db import conexao_banco

nome = 'Thayna'
telefone = '11 96370-5533'
email= 'thaynad781@gmail.com'
data_nascimento = '2007-08-11'
senha = '654321'

conexao = conexao_banco() #inicia a conexão com o banco

if conexao.is_connected():
    cursor = conexao.cursor()

    sql = """
    INSERT INTO cliente(nome, telefone, email, data_nascimento, senha)
        VALUES(%s,%s,%s,%s,%s)
    """
    dados = (nome,telefone, email, data_nascimento, senha)

    #execução de gravação
    cursor.execute(sql,dados)
    conexao.commit()

    #fechar a conexão com o banco
    cursor.close()
    conexao.close()
else:
    print('Falha de conexão com o banco')