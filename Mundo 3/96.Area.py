'''
Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''
def área(l,c):
    print(f'A área do terreno {l}x{c} é de {l*c} m²')
área(float(input("Insira a largura do terreno em metros: ")),float(input("Insira o comprimento do terreno em metros: ")))