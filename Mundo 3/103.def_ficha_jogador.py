'''
Exercício Python 103: Faça um programa que tenha uma 
função chamada ficha(), que receba dois parâmetros 
opcionais: o nome de um jogador e quantos gols ele 
marcou. O programa deverá ser capaz de mostrar a ficha 
do jogador, mesmo que algum dado não tenha sido 
informado corretamente.
'''
def ficha(nome="<desconhecido>",gols=0):
    print(f'\nO jogador(a) {nome} realizou {gols} gol(s) nos camponato!')

nome=input("\nInsira o nome do jogador:")
gols=input("Insira o número de gols do jogador:")

if nome =='' and gols !="":
    ficha(gols=gols)
elif gols=='' and nome!="":
    ficha(nome=nome)
elif nome=='' and gols=='':
    ficha()
else:
    ficha(nome,gols)