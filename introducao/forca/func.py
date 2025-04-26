import random
from os import path

def imprime_mensagem_abertura():
    print("****************************")
    print('A Forca"!!! ')
    print("****************************")

dicas = ('carro', 'cidade', 'país', 'nome', 'fruta')

def definir_tema():
    dica = int(input("""
        Digite a opção para jogar:
            1- Carros        
            2- Cidades do Brasil        
            3- Paises
            4- Nome de pessoas
            5- Frutas
        """))
    return dicas[dica - 1]

def carrega_palavra_secreta(tema):
    dirName = path.dirname(path.abspath(__file__))
    with open(f"{dirName}\\{tema}.txt", "r") as arquivo:
        palavras = [linha.strip() for linha in arquivo]
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]
