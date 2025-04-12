from xml.etree.ElementPath import xpath_tokenizer
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
from time import sleep
import os
from os import system, name


produto=input('Informe o produto: ')

# Para Ocultar a janela do navegador
#options = webdriver.ChromeOptions() 
#options.add_argument("--headless")
navegador = webdriver.Chrome()#(chrome_options=options)
url = f"https://www.mercadolivre.com.br/"
navegador.get(url)
sleep(3)
barraPesquisa=navegador.find_element_by_name("as_word")
barraPesquisa.send_keys(produto)
barraPesquisa.send_keys(Keys.ENTER)
sleep(2)
system('cls') if(name == 'nt') else system('clear')
listaProdutos = navegador.find_elements(By.CLASS_NAME, "ui-search-layout__item")
dadosExtraidos=[]
for item in listaProdutos:
    nome = item.find_element(By.CLASS_NAME, "ui-search-item__title").text
    preco = item.find_element(By.CLASS_NAME, "price-tag-fraction").text
    preco = preco.replace('.','')
    urlProduto=item.find_element(By.TAG_NAME, "a").get_attribute("href")
    dadosExtraidos.append((nome, preco, urlProduto))
#print(dadosExtraidos)

navegador.close()

arq = load_workbook("pesquisaPreço.xlsx")
planAtiva=arq['pesquisa']
for linha in dadosExtraidos:
   planAtiva.append(linha)

arq.save("pesquisaPreço.xlsx")

print('Dados extraídos e gravados com sucesso!!!')