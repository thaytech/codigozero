import requests

awesome_api = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"

requisicao = requests.get(awesome_api)
print(requisicao)


dolar_real =float(requisicao.json()['USDBRL']['bid'])
euro_real =float(requisicao.json()['EURBRL']['bid'])
bitcoin_real = float(requisicao.json()['BTCBRL']['bid'])

valor_real = float(input('Digite o valor em R$'))

print(f"{valor_real: .2f} em dólar $ {valor_real / dolar_real}")

print(f"{valor_real: .2f} em euro € {valor_real / euro_real}") 

print(f"{valor_real: .2f} em bitcoin  ₿ {valor_real / bitcoin_real}")


