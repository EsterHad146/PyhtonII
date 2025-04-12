from os import system
import random
system('cls')

print('********************')
print('ADIVINHE O NÚMERO')  
print('********************')

numero_secreto = random.randrange(0,101)
total_de_tentativas = 10

for rodada in range(1,total_de_tentativas + 1):
    print(f'\nTentativa {rodada:02d} de {total_de_tentativas:02d}')
    tentativa = input('Tente acertar o número de 1 a 100')
    print('Você digitou: ', tentativa)

    tentativa_int = int(tentativa)
    if(tentativa_int < 1 or tentativa > 100):
        print('Tentativa inválida! Somente números de 1 a 100')
        continue
    acerto = tentativa_int == numero_secreto
    maior = tentativa_int > numero_secreto
    menor = tentativa_int < numero_secreto
    if(acerto):
        print('Paraéns, você acertou!')
        break