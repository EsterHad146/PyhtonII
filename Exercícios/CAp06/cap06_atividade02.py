from os import system, name
def soma(x, y):
  try:
    print("Soma: ", float(x)+float(y))
  except:
    print("Ocorreu um erro")
  else:
    print('Executa sempre que o try não gera nenhum erro')
  finally:
    print('Executa sempre no final da estrutura try/except')

def subtracao(x, y):
  try:
    print("Subtracao: ", float(x)-float(y))
  except:
    print("Ocorreu um erro")

def multiplicacao(x, y):
  try:
    print("Multiplicacao: ", float(x)*float(y))
  except:
    print("Ocorreu um erro")

def divisao(x, y):
  try:
    print("Divisao: ", float(x)/float(y))
  except ZeroDivisionError as erro:
    print(erro)
  except:
    print("Ocorreu um erro")

opcao=1
while opcao:
  system('cls')
  x = input("Primeiro numero: ")
  y = input("Segundo numero: ")
  print("1. Somar")
  print("2. Subtrair")
  print("3. Multiplicação")
  print("4. Divisão ")

  operador = int(input("Opção: "))
  if(operador==1):
      soma(x, y)
  if(operador==2):
      subtracao(x, y)
  if(operador==3):
      multiplicacao(x, y)
  if(operador==4):
      divisao(x, y)

  opcao = input("\nAperte 0 para Sair ou Enter para continuar")
  if opcao=="0":
    opcao=int(opcao)
  else:
    opcao=1