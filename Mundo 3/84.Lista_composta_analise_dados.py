'''
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:                                                                                                    
A) Quantas pessoas foram cadastradas.                                                                                                                
B) Uma listagem com as pessoas mais pesadas.                                                                                                    
C) Uma listagem com as pessoas mais leves.
'''
import os
pessoas=list();pesos=[];
while True:
    pessoa=list(map(str,input("Insira o nome de uma pessoa e seu peso em Kg(ex: Fulano 80): ").split()))
    pessoas.append(pessoa)
    pesos.append(pessoa[1])
    if input("Deseja Continuar? (S/N) : ").upper() =='N' :
        break;

os.system('clear')
lista_ordenada_pesos= sorted(pessoas,key=lambda pessoa: pessoa[1])
print(f'Foram cadastradas {len(pessoas)} pessoas\n')

print("*"*30,"\nPessoas mais leves: ")
for i in range (len(lista_ordenada_pesos)//2):
    print(f'{lista_ordenada_pesos[i][0]} - {lista_ordenada_pesos[i][1]}Kg')

print("*"*30,"\nPessoas mais pesadas :")
for i in range (len(lista_ordenada_pesos)//2,len(lista_ordenada_pesos)):
    print(f'{lista_ordenada_pesos[i][0]} - {lista_ordenada_pesos[i][1]}Kg')