import csv

dados = 'veiculos.csv' # armazena o endereço do csv em uma variável

with open(dados, 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=',')

    print('Dados dos Veículos:\n')
    
    for linha in leitor:
     print(linha)

