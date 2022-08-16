'''
Exercício Python 104: Crie um programa que tenha a função 
leiaInt(),
que vai funcionar de forma semelhante ‘a função input() 
do Python, só que fazendo a validação para aceitar apenas um 
valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
'''

def leiaInt():
    n=input("\nInsira o um número inteiro: ")
    if not n.isdigit() :
        print("\n\033[31m ERRO! digite um número inteiro válido.\033[m")
        leiaInt()
    else:
        print(f"\nVocê acabou de digitar o número {n}")
leiaInt()
