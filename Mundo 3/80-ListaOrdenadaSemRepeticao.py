'''
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e 
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
No final, mostre a lista ordenada na tela.
'''

lista=[]

# for i in range(5):
#     numero=float(input("Insira um valor pra lista: "))

#     if i==0 or numero>lista[-1]:
#         lista.append(numero)
#         print(numero," foi add ao final da lista!")
#     elif i==1 or numero<lista[0]:
#         lista.insert(0,numero)
#         print(numero," foi add ao inicio da lista")
#     elif numero>lista[0] and numero<lista[1]:
#         lista.insert(1,numero)
#         print(numero, "foi add na posição 1 da lista")
#     elif numero>lista[1] and numero<lista[2]:
#         lista.insert(2,numero)
#         print(numero, " foi add na posição 2 da lista")
#     elif numero>lista[2] and numero<lista[-1]:
#         lista.insert(3,numero)
#         print(numero, " foi add na posição 3 da lista")
#     print(lista)
# print("Lista ordenada : ",lista)


#forma mais eficiente

for c in range(5):
    numero=float(input("Insira um número: "))
    if c==0 or numero>lista[-1]:
        lista.append(numero)
        print(f'O valor {numero} foi inserido ao final da lista com sucesso!')
    else:
        posi=0
        while posi<len(lista):
            if numero<=lista[posi]:
                lista.insert(posi,numero)
                print(f'O valor {numero} foi inserido na posição {posi} com sucesso!')
                break
            posi+=1

print("*"*30)
print(f'Os valores inseridos em ordem são = {lista}')