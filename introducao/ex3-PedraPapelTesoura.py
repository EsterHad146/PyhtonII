
from  os import system, name
import random

opcao = 's'
while opcao.upper()=='S':
    system('cls') if(name == 'nt') else('clear')

    computador= random.randint(0,2)
    jogador = int(input('''Escolha uma opção para jogar: 
        [1] Pedra
        [2] Papel
        [3] Tesoura
        Digite sua escolha: ''')) -1
    pecas = ('Pedra, Papel, Tesoura')
    
    tabela =(
        ('NINGUEM', 'JOGADOR', 'CPU'),
        ('CPU','NINGUEM', 'JOGADOR'),  
        ('JOGADOR', 'CPU','NINGUEM')
    )
    
print(f'Você escolheu {pecas[jogador]}')
print(f'Computador escolheu {pecas[computador]}')
print(f'Resultado: {tabela[computador],[jogador]} Ganhou!')
opcao = input('Jogar Novamente? Aperte (S)Sim para jogar!')

