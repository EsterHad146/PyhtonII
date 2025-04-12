"""
  Cap05 - Atividade 02
  Jogo: Papel, pedra e Tesoura

  Objetivos:
  Nesta atividade você vai criar um jogo usando 
  tupla e tupla multi-dimensional.

  Comandos utilizados:
  Tupla, Tupla Multi-Dimensional, biblioteca random e randint
"""
from os import system, name
# biblioteca random
import random

opcao = 's'
while opcao.upper()=='S':
    system('cls') if(name == 'nt') else system('clear')

    computador = random.randint(0,2)
    jogador = int(input('''Escolha uma opcao para se jogar: 
    [0] Pedra
    [1] Papel
    [2] Tesoura
    Digite sua escolha: '''))

    pecas = ("Pedra", "Papel", "Tesoura")

    if (jogador >= 3):
        resultado = 'Você não escolheu um item correto!!!'
    else:
        print('Você escolheu {}' . format(pecas[jogador]))
        print('O computador escolheu: {}' . format(pecas[computador]))
        # lista multi-dimensional
        # nesta lista quando o resultado for -1 o computador ganha, 1 o jogado ganha e 0 deu empate
        tabela = ((0, 1, -1),(-1, 0, 1),(1, -1, 0)) #Só sei que foi assim
        jogada = tabela[computador][jogador]
        match jogada:       #Funciona apenas a partir da versão 3.7
            case 0:
                resultado = "Deu empate vocês escolheram a mesma peça"
            case 1:
                resultado = "Você ganhou!"
            case -1:
                resultado = "O computador ganhou"

    print(resultado)
    opcao=input('Jogar novamente? Aperte S(sim) para jogar novamente. ')