"""
  Cap02 - Atividade 01
  Objetivo receber e somar dois 
  números armazena-los em  variaveis 
  e exibir o resultado

"""
#Limpar a tela
import os
os.system('cls' if os.name=='nt' else 'clear')

print("Seja Bem vindo!")
print("Vamos fazer a soma de dois números inteiros.")
#Entradas
numero1=input('Informe o 1º numero: ')
numero2=input('Informe o 2º numero: ')
#Processamento
soma = numero1+numero2
#SAída
print('A soma entre {} e {} é igual a {}'.format(numero1, numero2, soma))
#O comando TYPE verifica o tipo de uma variável
print(f'Os tipos das variaveis que recebem a resposta de um input são do tipo {type(numero1)}')
print('É necessário converter')
#-------------------------------
#Processamento
soma = int(numero1)/int(numero2)
print(type(soma))
#SAída
print('A soma entre {} e {} é igual a {}'.format(numero1, numero2, soma))
