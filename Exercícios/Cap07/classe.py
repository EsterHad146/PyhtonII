#Classe Produto
class Produto:
    def __init__(self, marca, descricao, preco, disponivel):
        self.marca=marca
        self.descricao=descricao
        self.preco=preco
        self.disponivel=disponivel
    def verProduto(self):
        print(f'{self.descricao} {self.marca} por apenas R${self.preco:.2f}. Produto disponível? {self.disponivel}')

class Calculadora:  
    def __init__(self, valor1, valor2):
        self.valor1=valor1
        self.valor2 =valor2
    def soma(self):
        return self.valor1 + self.valor2
    def sub(self):
        return self.valor1 - self.valor2
    def mult(self):
        return self.valor1 * self.valor2
    def div(self):
        return self.valor1 / self.valor2