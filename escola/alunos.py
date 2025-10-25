import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "escola"
)

cursor = conexao.cursor()

def inserir_aluno(nome, idade,email):
    sql = "INSERT INTO alunos (nome,idade,email) VALUES (%s,%s,%s)"
    cursor.execute(sql,(nome, idade, email))
    conexao.commit ()
    print("Aluno inserido com sucesso!")

def listar_alunos():
    cursor.execute("SELECT * FROM alunos")
    for linha in cursor.fetchall():
        print(linha)

def deletar_aluno(id):
    sql = "DELETE FROM alunos WHERE id=%s"
    cursor.execute(sql,(id))
    conexao.commit()
    print("Aluno deletado com sucesso!")

def atualizar_aluno(id, novo_nome, nova_idade, novo_email):
    sql = "UPDATE alunos SET  nome=%s, idade=%s, email=%s WHERE id=%s"
    cursor.execute(sql,(novo_nome, nova_idade, novo_email, id))
    conexao.commit()
    print("Aluno atualizado com sucesso!")

if __name__ == "__main__":

    #inserir_aluno("Rayka", 18, "rayray@gmail.com")
    #listar_alunos()
    #deletar_aluno(7)
    atualizar_aluno(2, "Fernanda", 20, "fefe@gmail.com")


cursor.close()
conexao.close()
