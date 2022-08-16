'''
Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. 
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, 
o programa se encerrará. Importante: use cores.
'''
from funcoes_listas import escreva
import os
#não ficou mt bom deve ficar no windows
def interactive_helping_system():
    while True:
        escreva("SISTEMA DE AJUDA PyHELP",'31')
        menu=input("Função ou biblioteca: ")
        escreva(f"Acessando o comando {menu}",'32')
        print("\033[2;31;45m")
        help(menu)
        print("\033[m")
        sair=input("Desenha sair? s/n ").upper()
        if sair=='S':
            escreva('FIM','31')
            break;

interactive_helping_system()
