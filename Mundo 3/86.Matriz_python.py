'''
Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores 
lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
'''
matriz=[[[],[],[]],
        [[],[],[]],
        [[],[],[]]]

for i in range(3):
    for j in range(3):
        matriz[i][j]=int(input(f"Insira um número para a posição {i}{j} da matriz!: "))
print("Matriz gerada: \n")
for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]:^5}]",end="")
        print(end="")
    print("\n")
