'''
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
infos=dict()

infos['nome']=input("insira o nome do jogador: ")

N_partidas=int(input(f"Quantas partidas {infos['nome']} jogou? "))

gols=[];total=0;
for i in range(N_partidas):
    gols.append(int(input(f"Quantos gols na partida {i}: ")))
infos['gols']=gols
infos['total']=sum(gols)

print("=-"*30)
print(infos)
print("=-"*30)
for k,v in infos.items():
    print(f"O campo {k} tem valor {v}")
print("=-"*30)   
print(f"\n O jogador {infos['nome']} jogou {N_partidas} partidas:")
for i, v in enumerate(infos['gols']) :
    print(f'\t partida {i} : {v} gols')
print(f"Ocorreram no total {infos['total']} gols")