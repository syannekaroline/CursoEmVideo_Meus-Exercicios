
'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''
import random
print("=-"*30);print("{:^60}".format("JOGO DA MEGA SENA"));print("=-"*30)
N_jogos=int(input("quantos jogos serão gerados? "))
jogos_gerados=list()
for i in range(N_jogos):
    jogo=list()
    for i in range(6):
        n=random.randint(1,60)
        if n in jogo:
            n=random.randint(1,60)
        jogo.append(n)
    jogos_gerados.append(sorted(jogo))
print(f"Jogos gerados:\n")
i=0
for jogo in jogos_gerados:
    i+=1
    print(f"{i} Jogo: {jogo}")