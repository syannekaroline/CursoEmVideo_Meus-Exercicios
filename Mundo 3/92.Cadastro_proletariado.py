'''
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
import datetime
dados=dict()

dados['nome']=input("insira o nome do trabalhador: ")
dados['nascimento']=int(input("insira o ano de nascimento: "))
dados['CTPS']=input("insira o número da cardeira de trabalho:(0 não tem) ")
dados['idade']= datetime.datetime.now().year - dados['nascimento']

if dados['CTPS']!='0':
    dados['ano_contratação']=int(input("Insira o ano de contratação: "))
    dados['salário']=float(input("Insira o salário atual: R$"))
    dados['Se aposenta com essa idade']=dados['idade']+ ((dados['ano_contratação']+35)-datetime.datetime.now().year)

for k,v in dados.items():
    print(f'{k} : {v}')

