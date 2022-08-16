'''
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
 Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, 
 sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint
from funcoes_listas import Imprimi_lista_dicts
infos=dict()

for i in range(4):
    infos[input(f"Insira o nome do jogador {i+1} : ")] = randint(1,6)

print("{:^10}|{:^10}".format("Jogador",'valor'))

for k in sorted(infos,key= infos.get,reverse=True):
    if infos[k] == max(list(infos.values())):
        print(f'\033[32m{k:^10}|{infos[k]:^10} - vencedor \033[m')
    else :
        print(f'\033[34m{k:^10}|{infos[k]:^10}')

