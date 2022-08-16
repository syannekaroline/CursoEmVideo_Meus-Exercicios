'''
Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
'''
from utilidadesCeV import moedas

preco=float(input("Insira um preço: R$"))

print(f"{preco} após aumento de 10% : {moedas.aumentar(preco,10):.2f}")
print(f"{preco} após diminuição de 10% : {moedas.diminuir(preco,10):.2f}")
print(f"O dobro de R${preco:.2f} : R${moedas.dobro(preco):.2f}")
print(f"A metade de R${preco:.2f} : R${(moedas.metade(preco)):.2f}")