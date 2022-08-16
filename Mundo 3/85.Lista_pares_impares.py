'''
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''
from funcoes_listas import Gera_lista, N_impares_lista, N_pares_lista,imprimi_lista
print("Digite 7 os valores para a lista: ")

lista=Gera_lista()
print(f'Lista gerada: {lista}')
print(f'Os valores pares em ordem crescente digitados foram: {sorted(N_pares_lista(lista))}')
print(f'Os valores ímpares em ordem crescente digitados foram: {sorted(N_impares_lista(lista))}')