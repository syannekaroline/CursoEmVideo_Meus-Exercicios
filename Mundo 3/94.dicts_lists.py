'''
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média
'''
dados=list();pessoa=dict();idades=[]
while True:
    pessoa['nome']=input('Insira o nome: ')
    pessoa['sexo']=input('Insira o sexo[f/m]: ').upper()
    pessoa['idade']=int(input('Insira a idade: '))
    idades.append(pessoa['idade'])
    dados.append(pessoa.copy())
    c=input("Deseja cadastrar mais uma pessoa? [s/n]").upper()
    if c=='N':
        break;

print("=-"*40)
print(f"\nForam cadastradas {len(dados)} pessoas")
print(f"Média das idades {sum(idades)/len(idades)}")
print('lista das mulheres: ')
for i in dados:
    if i['sexo'] == 'F':
        print(f"\t{i['nome']}")
print("Pessoas com idade acima da média")
for i in dados:
    if i['idade'] > sum(idades)/len(idades):
        print(f"\t{i['nome']}")