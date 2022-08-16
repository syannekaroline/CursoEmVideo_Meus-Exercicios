'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''
from funcoes_listas import Gera_lista,N_pares_lista, N_impares_lista
lista=Gera_lista()
print(f'Valores da lista : {lista}')
N_pares=N_pares_lista(lista)
N_impares=N_impares_lista(lista)
print(f'Números Pares da lista: {N_pares}\nNúmeros ìmpares da lista :{N_impares}')