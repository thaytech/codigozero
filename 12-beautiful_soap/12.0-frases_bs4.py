# Extraindo frases de um site e salvando em um arquivo de texto
import bs4 #importa a biblioteca BeautifulSoup 4
import requests #importar a biblioteca requests

url = 'https://quotes.toscrape.com/' #grava o site quotes
quotes = requests.get(url) #importa o codigo do site
soup = bs4.BeautifulSoup(quotes.text, 'html.parser') #coverte o quote em html

# frase = soup.find('div', class_='quote') #procura a div com a class quote
frase = soup.find_all('div', class_='quote')

# Loop para pegar todas as frases
for div in frase:
    texto = div.find('span', class_='text') #procura a tag span com a class text
    print(texto)

# Salvando as frases em um arquivo de texto
for div in frase:
    texto = div.find('span', class_='text').text
    with open('12-frases.txt', 'a', encoding="utf-8") as arquivo:
        arquivo.write(f'{texto} \n')