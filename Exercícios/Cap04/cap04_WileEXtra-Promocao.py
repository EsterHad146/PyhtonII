'''
    Promoção!!!
    O algorítimo deve diariamente aplicar o desconto 
    no preço de um produto até atingir o preço de custo.
    
    Comandos utilizados: While, variavel contadora, 
    incrementação e decrementação de variaveis
'''
from os import system, name
system('cls') if(name == 'nt') else system('clear')

produto='Notebook'
precoVenda = 3000
precoCusto = 1800
desconto = 100
cont=0
while precoVenda > precoCusto:
    cont+=1
    print(f'No {cont}º dia da promoção o preco do {produto} é de: {precoVenda}')
    precoVenda-=desconto