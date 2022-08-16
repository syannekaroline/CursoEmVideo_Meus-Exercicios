'''Exercício Python 115a: Vamos criar um menu em Python, usando modularização.'''

from utilidadesCeV import interface,arquivotxt
if not arquivotxt.ArquivoExiste('registros.txt'):
    arquivotxt.criar_txt('registros.txt')
while True:
    opcao=interface.Intercafe("menu principal",['Ver Pessoas Cadastradas','Cadastrar Novas Pessoas','Sair do Sistema'])
    if opcao==1:
        arquivotxt.ler_txt('registros.txt')
    if opcao==2:
        nome=input("Insira o nome: ")
        idade=interface.leiaInt("Insira a idade: ")
        arquivotxt.cadastrar_txt('registros.txt',nome,idade)
    if opcao==3:
        interface.cabecalho("Obrigada! Volte Sempre",35)
        break
