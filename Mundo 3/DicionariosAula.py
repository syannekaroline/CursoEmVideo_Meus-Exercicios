'''
Dicionários:
são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais
dicionários são identificados por chaves
'''

#identificados por chaves {}
dados={}
dados2=dict()
dados={'nome':"syanne",'idade':25}
print(f"Nome : {dados['nome']} | Idade: {dados['idade']}")

#add elementos
dados['sexo']= 'F'
print(dados)

#removendo elemento
del dados['sexo']

print(f" Após remover a info do sexo: {dados}")

#mostrando elementos do dicionário:

print(f"Mostra todos os valores: \n{list(dados.values())}")
print(f'Mostrar todas as chaves do dicionário : \n{list(dados.keys())}')
print(f"Mostrar todos os itens do dict : \n{list(dados.items())}")

#podem ser usados em loops for para acesso ao conteúdo dos dicionários

for k,v in dados.items():
    print(f"{k}-{v}")

#pode-se usar estruturas compostas de listas de dicionários 

materias=[{'matemática':10},{'literatura':9.9}]

for i,valor in enumerate(materias):
    print(f"\n{i} - {list(valor.keys())[0]}- {list(valor.values())[0]}")

#parar fazer cópia de um elemento do dicionário não se pode usar fatiamento, se usa um método interno .copy()

estado=dict();brasil=list()

for c in range(3):
    estado['uf']=str(input("Insira uma unidade federativa: "))
    estado['sigla']=input("Insira a sigla: ")
    brasil.append(estado.copy())

for i,valor in enumerate(brasil):
    print(f"\n{i} - {list(valor.keys())[0]}- {list(valor.values())[0]}")

#organizando dicionário 
from operator import itemgetter
notas={'calculo':8.5, 'probabilidade':9.9,'Programação':10}
notas=sorted(notas.items(),key=itemgetter(1),reverse=True)
print(notas)
