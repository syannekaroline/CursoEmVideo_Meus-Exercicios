'''
Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''
dado=dict()

dado['nome']=input("Insira o nome do aluno : ")
dado['média']=float(input("Insira a média no aluno: "))

if dado['média'] >= 7.0:
    dado['situação']="Aprovado"
elif dado['média']>=5 and  dado['média']<7: 
    dado['situação']='Recuperação'
else:
    dado['situação']='Reprovado'
      


for k, v in dado.items():
    print(f"\033[33m{k}\033[m = {v}")