'''
Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''
def fatorial(num=1,show=False):
    f=1  
    for i in range(num,0,-1):
        if show:
            print(f'{i}.',end="")
            print("=",end="")
        f*=i
    return f
num=int(input("Insira um número para ver seu fatorial: "))
show=input("Deseja visualizar o cálculo? [s/n]").upper()
show= True if show=='S' else False  
print(" ",fatorial(num,show))