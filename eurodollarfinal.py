import requests
import json
import datetime

requisição = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL,EUR-BRL,BTC-BRL')

cotacao = json.loads(requisição.text)

print("**********Cotação do Dolar**********")
print(datetime.datetime.now())
print("O maior valor do dolar foi")
print(cotacao['USD']['high'])
print("o menor valor do dolar foi")
print(cotacao['USD']['low'])
print("A variação em ficou em ")
print(cotacao['USD']['varBid'])