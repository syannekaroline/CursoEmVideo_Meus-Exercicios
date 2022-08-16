'''
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:                                                                                                                                                
A) Quantos números foram digitados.                                                                                                                    
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''
import os
lista=[]
while True :
    numero=input("Digite um número pra uma lista (Digite 'P' para parar de inserir): ")
    if numero.upper() =="P":
        break
    lista.append(float(numero))
os.system("clear")
print(f"Foram digitados {len(lista)} números")
print(f"lista gerada : {lista}")
print(f"lista de valores ordenada de forma decrescente: {sorted(lista,reverse=True)}")

n = int(input("Insira um número pra saber se ele está contifdo ou não na lista: "))
print(f"O valor {n} está contido na lista") if n in lista else print(f"O valor {n} não está contido na lista")