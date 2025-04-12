#Consumir a classe produto
from classe import Produto
notebook = Produto('Dell','Notebook I7', 5800.9, 'Sim')
celular = Produto('Xiaomi','Read MI Note 12', 2500.8, 'Não')
input('Pressione qualquer tecla para ver a oferta: ')
notebook.verProduto()
celular.verProduto()
print()