'''
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), 
que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens 
através da função criada:                                                                                                                                                                            
a) de 1 até 10, de 1 em 1                                                                                                                                              b) de 10 até 0, de 2 em 2                                                                                                                                            Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:                                                                                                                                                                            a) de 1 até 10, de 1 em 1                                                                                                                                              
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
from time import sleep
def linha():
    print("*"*30)
def contador(inicio,fim,passo):
    print('\n')
    linha()
    print(f"\nContagem de {inicio} até {fim}, de {passo} em {passo}  :")
    for i in range(inicio,fim+1,passo):
        print(i," ",end='',flush=True)
        sleep(0.5)
    print("FIM")

contador(1,10,1)
contador(10,0,-2)
print("\ncontagem personalizada")
contador(int(input("Insira o inicio da contagem: ")),int(input("Insira o fim da contagem: ")),int(input("Insira o passo da contagem: ")))


