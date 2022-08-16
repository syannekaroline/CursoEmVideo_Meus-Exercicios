'''
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''
notas=list()
while True:
    aluno=list()
    nome=input("Insira o nome do aluno: ")
    n1,n2=input("Insira as duas notas serapadas por um espaço: ").split()
    aluno.extend([nome,n1,n2])
    notas.append(aluno)
    if input("Deseja cadastrar mais um aluno (s/n)? ").upper() =='N': break;
print("-="*50,"\n")
print("{:^20}|{:^20}".format("Aluno","Média"))
for aluno in notas:
    print(f'{aluno[0]:^20}|{(float(aluno[1])+float(aluno[2]))/2:^20}')
while True:
    nome=input("Insira o nome de um aluno pra acessar suas notas individuais (00 pra parar): ")
    if nome=="00":
        break
    for aluno in notas:
        if nome==aluno[0]:
            print(f'{aluno[0]}  | nota 1 = {aluno[1]} |nota 2 : {aluno[2]}')
            break;
        print("Esse aluno não foi registrado no cadastro de notas! ")