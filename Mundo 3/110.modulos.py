'''Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.'''

from utilidadesCeV import moedas

preco=float(input("Insira um preço: R$"))

moedas.resumo(preco)