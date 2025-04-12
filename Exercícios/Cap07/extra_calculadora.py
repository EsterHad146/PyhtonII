from classe import Calculadora
valor1 = int(input('Informe o 1º valor: '))
valor2 = int(input('Informe o 2º valor: '))
calc = Calculadora(valor1, valor2)
input()
print(calc.valor1)
print(calc.valor2)

print('------------------')
print('Soma: ', calc.soma())
print('------------------')
print('Subtração: ', calc.sub())
print('------------------')
print('Multiplicação: ', calc.mult())
print('------------------')
print('Divisão: ', calc.div())

input()