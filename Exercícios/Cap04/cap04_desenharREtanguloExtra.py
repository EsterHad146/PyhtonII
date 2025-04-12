'''
    Criar um retangulo utilizando um símbolo
    Ex.:
    @@@@@@
    @@@@@@
    @@@@@@
    @@@@@@
    @@@@@@
    @@@@@@

'''
linhas = int(input('Informe o nº de linhas: '))
colunas=int(input('Informe o nº de colunas: '))
char=input('Informe o caractere desejado: ')
for l in range(linhas):
    for c in range(colunas):
        print(char[0], end='')
    print()