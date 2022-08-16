'''
Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e 
dizer qual deles é o maior.
'''
def maior(*inteiros):
    print("Maior valor recebido foi: ",max(inteiros[0]))

maior(input("Insira valores separados por espaço pra saber qual o maior entre eles: ").split())