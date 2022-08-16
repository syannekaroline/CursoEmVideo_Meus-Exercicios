from re import S
from funcoes_listas import Imprimi_lista_dicts
dados=list()
infos=dict()

while True:

    infos['nome']=input("insira o nome do jogador: ")

    N_partidas=int(input(f"Quantas partidas {infos['nome']} jogou? "))

    gols=[];total=0;
    for i in range(N_partidas):
        gols.append(int(input(f"Quantos gols na partida {i}: ")))
    infos['gols']=gols
    infos['total']=sum(gols)
    dados.append(infos.copy())
    if input("Deseja continuar: [S/N]: ").upper() == 'N':
        break;

print(dados)
for i ,v in enumerate(dados): 
    print(i,v)
    print(v['nome'])
    print(v['total'])
    print("{:^20}|{:^20}|{:^20}|{:^20}".format('cod','nome','gols','total de gols'))
    print(f"{i:^20}|{v['nome']:^20}|\t{v['gols']}\t|{v['total']:^20}")