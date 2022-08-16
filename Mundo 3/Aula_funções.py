'''
funções ou rotinas e como utilizar funções em Python. Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python. Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.
'''

#criar função persolizada são declaradas com def na frente

def cabecalho(msg):
    print("-="*30)
    print(f"{msg.upper():^60}")
    print("-="*30)

cabecalho('syanne')

#empacotar parâmetros - quando não se sabe o número de parâmetros que irão passar
def contador(*parametros):
    print(f'recebi os parâmetros :{parametros}')#retora uma tupla com os parâmetros recebidos
contador(1,2,3,4,'s')

def dobra(lista):
    for i,v in enumerate(lista):
        lista[i]=v*2
lista=[1,2,3,4]
print(lista)
dobra(lista)
print(lista)

#Interactive help
#ajuda interativa 
# help(print)#manual de ajuda, mostra como funciona qualquer comando, qualquer função ou biblioteca interna, pra sair dijitar exist() ou quit
#outra forma de fazer seria print(print.__doc__)
# print(input.__doc__)

#docstrigs
# é uma string de documentação como os manuais no interactive help - para fazer basta abrir aspas duplas na linha após a declaração da função
def exemplo():
    '''
    Essa é uma função de exemplo pra mostrar como funcionan as docstrings
    '''


#argumentos opcionais
#atribuir um valor pra um parâmetro da declaração da função, caso a função não receba aquile parâmetro ao ser chamada, ela irá receber o valor definido na sua declaração 
def somar_3_N(a=0,b=0,c=0):
    soma=a+b+c
    print(f" a soma vale {soma}")
somar_3_N()

#escolpo de variáveis
    #local onde uma variável vai existir ou local onde ela não vai existir
    #para usar uma variável global dentro da função diretamente, usa-se global
def teste(b):
    global g
    g+=2
    n=0 # esse n é uma nova variǘel local
    b+=1
    x=8#neste caso x só válido dentro da função, é uma variável local
    print(f"Na função teste n global vale {b-1}")
    print(f"Na função teste a variável n local vale {n}")
    print(f"Na função teste b vale {b}")
    print(f"Na função teste x tem valor {x}")
    print(f"Na função global g tem valor {g}")

n=2
g=20
print(f'No programa principal n vale {n}')

#escolpo de chamada de função


teste(n)
print(g)
#mesmo n sendo declarado fora da função seu valor é válido em todo o programa- escolpo global

#retorno das funções 
#função tem um retorno que pode ser atribuído a uma variável ou oude ser printado, são úteis quando se quer personalização dos resultados