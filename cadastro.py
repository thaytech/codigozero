NOME_PROGRAMA = "AGENDA DE CONTATOS"

agenda = []  #Lista para armazenar os contatos

def cadastrar_contato(nome):
    agenda.append(nome)  # Adiciona o contato a agenda
    print(f"Contato '(nome)'Cadastrado com sucesso")

def listar_contatos():
    print("Lista de contatos")
    print(agenda)

def remover_contato():
    contato = input("Qual contato deseja remover da agenda: ")
    if contato in agenda:
        agenda.remove(contato)  #Remove o contato da agenda
        print(f"Contato{contato} removido com sucesso")
    else:
        print(f"Contato {contato}não encontrado na agenda")

def main():
    while True: 
        print("")
        print(NOME_PROGRAMA)
        print("-" * 20)
        print("Menu: ")
        print ("1. Cadastrar Contato")
        print("2. Listar Contato")
        print("3. remover Contato")
        print("4. Sair")
        print("-" * 20)

        opcao = input("Escolha uma opção: ")

        if opcao == "1" :
            nome = input ("Digite um nome para incluir na agenda: ")
            cadastrar_contato(nome)
        elif opcao == "2" : 
            listar_contatos()
        elif opcao == "3" :
            remover_contato()
        elif opcao == "4" :
            break 
        else: 
            print("Opção inválida, tente novamente")
#Linha padrão que executa nosso programa
if __name__ == "__main__":
    main()