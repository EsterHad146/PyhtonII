"""
    Raspagem de dados utilizando o serviço de pesquisa do google e as bibliotecas selenium e autogui

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
import pyautogui as gui
from datetime import datetime
import os
from os import system, name
system('cls') if(name == 'nt') else system('clear')

def capturarValorMoeda(moeda, elementoAlvo):
    url = f"https://www.google.com/search?q={moeda}+hoje"
    navegador.get(url)
    #gui.sleep(2)
    cotacao=navegador.find_elements(By.XPATH, elementoAlvo)
    return cotacao[0].text

# Para Ocultar a janela do navegador
#options = webdriver.ChromeOptions() 
#options.add_argument("--headless")
navegador = webdriver.Chrome() #(chrome_options=options)

elementoAlvo = '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
cotacaoDolar = capturarValorMoeda('dolar', elementoAlvo)
elementoAlvo = '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
cotacaoEuro= capturarValorMoeda('euro', elementoAlvo)
elementoAlvo='//*[@id="crypto-updatable_2"]/div[3]/div[2]/span[1]'
cotacaoBitcoin=capturarValorMoeda('bitcoin', elementoAlvo)
agora = datetime.now()
dataAtual= agora.strftime("%d/%m/%Y")
horaAtual= agora.strftime("%H:%M:%S")

print(f'Data: {dataAtual} | Hora: {horaAtual}\n Dolar: {cotacaoDolar}\n Euro: {cotacaoEuro}\n Bitconin: {cotacaoBitcoin}\n')
navegador.close()
arq = load_workbook("Cotações.xlsx")
planAtiva=arq['Cotações']
dados = ((dataAtual, horaAtual, cotacaoDolar, cotacaoEuro, cotacaoBitcoin))
planAtiva.append(dados)
arq.save("Cotações.xlsx")

print('As cotações foram importadas e gravadas com sucesso!!!')


''' 
url="https://www.google.com.br/"
navegador.get(url)
navegador.find_element_by_name("q").send_keys("Dolar hoje")
navegador.find_element_by_name("q").send_keys(Keys.ENTER)
elementoAlvo = '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
cotacaoDolar=navegador.find_elements_by_xpath(elementoAlvo)[0].text 

'''
