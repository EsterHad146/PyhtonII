"""
  Cap06 - Atividade 04
  Função de Datas

  Objetivos:
  Nesta atividade você vai aprender a usar a biblioteca 
  datetime do python, com ela é 
  possível manipular datas e converter uma string em data. 
  E irá implementar um return numa função.
  
  Comandos utilizados:
  Biblioteca datetime, metodos strptime, strftime e today. Função com return
  
  https://docs.python.org/3/library/functions.html
"""
from datetime import datetime

def idade(nascimento):
  today = datetime.today()
  return today.year - nascimento.year - ((today.month, today.day) < (nascimento.month, nascimento.day))

#def idade(nascimento): 
    #diasAno = 365.2425    
    #idade = int((datetime.today() - nascimento).days / diasAno) 
    #return idade 

def dias(nascimento):
  today = datetime.today()
  return abs((nascimento - today).days)

print(datetime.now())
atual = datetime.now()
print('Tipo de dado atual: ' , type(atual))
montarData = datetime(2021, 10, 5)
print('Tipo de dado atual após montar data', type(montarData))
print(atual.strftime('%d/%m/%Y %H:%M'))
dataNascimento = input('Informe a sua data de nascimento dd/mm/aaaa: ')
dataNascimento = datetime.strptime(dataNascimento, '%d/%m/%Y')
print(f'Você tem: {idade(dataNascimento)} anos')
print(f'Você já viveu {dias(dataNascimento)} dias')