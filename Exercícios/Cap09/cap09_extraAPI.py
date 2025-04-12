import requests

url="https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
cotacoesJson = requests.get(url)
cotacoesDic = cotacoesJson.json()
#print(cotacoesDic)
print('Cotações das principais moedas: ')
dolar = cotacoesDic['USDBRL']['bid']
print('Cotação do dolar: ', dolar)
euro = cotacoesDic['EURBRL']['bid']
print('Cotação do euro: ', euro)
bitcoin = cotacoesDic['BTCBRL']['bid']
print('Cotação do bitcoin: ', bitcoin)

print('#############################################################')
url="https://api.openweathermap.org/data/2.5/weather?appid=9e2aa2e6c8bf8537aa1e1414432a4007&q=sao+paulo,br&units=metric&lang=pt_br"
varMeteorJson=requests.get(url)
varMeteorDic=varMeteorJson.json()
#print(varMeteorDic)
print('Dados Meteriológicos: ')
print('Cidade: ', varMeteorDic['name'])
print('Temperatura', varMeteorDic['main']['temp'])
print('Status', varMeteorDic['weather'][0]['description'])