#funções recorrentes envolvendo listas

def Gera_lista():
    '''função que retorna uma lista com valores inteiros recebidos em uma mesma linha.'''
    lista=list(map(int,input("Insira valores Numéricos pra uma lista separados por um espaço: ").split())) 
    return lista

def Gera_lista_verificador():
    '''função que recebe valores flutuantes pra uma lista com verificação de continuação de entrada'''
    lista=[]
    while True :
        numero=input("Digite um número pra uma lista (Digite 'P' para parar de inserir): ")
        if numero.upper() =="P":
            break
        lista.append(float(numero))
    return lista

def N_pares_lista(lista):
    '''função que recebe uma lista e retorna os seus números pares
'''
    pares=list()
    for numero in lista:
        if numero%2==0:
            pares.append(numero)
    return pares

def N_impares_lista(lista):
    '''função que recebe uma lista de números e retorna os seus valores ímpares'''

    impares=list()
    for numero in lista:
        if numero %2 != 0 :
            impares.append(numero)
    return impares

def imprimi_lista(lista):
    for i in lista:
        print(i)

def imprimi_lista_indice(lista):
    print("key - item")
    for indice, valor in enumerate(lista) :
        print(f'{indice} - {valor}')

def Imprimi_lista_dicts(lista,key,value):
    '''função que recebe como parâmetro uma lista de dicionários e o cabeçalho dos dicionários(ao que se referem as chaves e os valores) e imprime na forma de tabela o conteúdo de forma formatada
'''
    print("{:^10}|{:^10}|{:^10}".format("Índice",key,value))
    for i,valor in enumerate(lista):
        print(f"\n{i:^10}|{list(valor.keys())[0]:^10}|{list(valor.values())[0]:^10}")

def escreva(msg,cod):
    n=len(msg)+4
    print(f"\033[1;{cod};45m\n")
    print('*'*n)
    print('  {}  '.format(msg))
    print('*'*n)
    print(f"\033[m",end="")
