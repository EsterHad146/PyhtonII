"""
  Cap04 - Atividade 02
  MultiTabuada

  Objetivos:
  Nesta atividade você vai construir uma multitabuada de duas maneiras, na primeira usando for e na segunda usando for aninhado

  Comandos utilizados:
   Comandos for range
"""
from os import system, name
system('cls') if(name == 'nt') else system('clear')

print('*** MULTI TABUADA 1 ***\n')
for i in range(1, 11):
  print(f'{i:>4}, {i*2:>4}, {i*3:>4}, {i*4:>4}, {i*5:>4}, {i*6:>4}, {i*7:>4}, {i*8:>4}, {i*9:>4}, {i*10:>4}')

print('\n*** MULTI TABUADA 2 ***')
# usando um for dentro de outro
for i in range(1, 11):
  linha = f'{i: >4}'
  for ii in (range(2, 11)):
    linha+=f'{ii*i: >4} '
  print(linha) 