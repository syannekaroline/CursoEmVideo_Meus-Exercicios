'''
Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
'''
from utilidadesCeV import moedas

preco=float(input("Insira um preço: R$"))

print(f"{moedas.moeda(preco)} após aumento de 10% : {moedas.moeda(moedas.aumentar(preco,10))}")
print(f"{moedas.moeda(preco)} após diminuição de 10% : {moedas.moeda(moedas.diminuir(preco,10))}")
print(f"O dobro de {moedas.moeda(preco)} : {moedas.moeda(moedas.dobro(preco))}")
print(f"A metade de {moedas.moeda(preco)} : {moedas.moeda(moedas.metade(preco))}")