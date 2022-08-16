'''
Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
'''
from utilidadesCeV import moedas

preco=float(input("Insira um preço: R$"))

print(f"{moedas.moeda(preco)} após aumento de 10% : {(moedas.aumentar(preco,10,format=True))}")
print(f"{moedas.moeda(preco)} após diminuição de 10% : {moedas.diminuir(preco,10,format=True)}")
print(f"O dobro de {moedas.moeda(preco)} : {moedas.dobro(preco,format=True)}")
print(f"A metade de {moedas.moeda(preco)} : {moedas.metade(preco,format=True)}")