'''
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:                                                    
A) A soma de todos os valores pares digitados.                                                                                                  
B) A soma dos valores da terceira coluna.                                                                                                                
C) O maior valor da segunda linha.
'''
matriz=[[[],[],[]],
        [[],[],[]],
        [[],[],[]]]
a=b=c=0
for i in range(3):
    for j in range(3):
        matriz[i][j]=int(input(f"Insira um número para a posição {i}{j} da matriz!: "))
        if matriz[i][j] %2==0:
            a+=matriz[i][j]
        if i==2:
            b+=matriz[i][j]
print("Matriz gerada: \n")
for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]:^5}]",end="")
        print(end="")
    print("\n")

print(f"Soma de todos os valores pares inseridos : {a}")
print(f"Soma de todos os valores da terceira linha : {b}")
print(f"Maior valor da segunda linha : {max(matriz[2])}")