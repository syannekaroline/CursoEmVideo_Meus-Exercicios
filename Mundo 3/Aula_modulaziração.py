#módulos e pacotes
#divide programas mt grandas, aumenta a legibilidade, facilita a manutenção

#separar em um arquivo .py apenas as funções e pode importa-las pra qualquer outro arquivo usando o import "nome do arquivo" 

import funcoes_listas
from funcoes_listas import Gera_lista

funcoes_listas.escreva("syanne",31)
print(Gera_lista())

#pacotes - bibliotecas
#se tiver muitas funções dentro do arquivo funções.py pode-se dividir essas funções em pacotes por exemplo separados por assunto
#em python toda pasta é considerada um pacote
#ex: pasta - uteis, dentro de uteis tem várias outras pastas separadas por assuntos ex: pasta números, datas, strings, cores
#existe uma sintaxe pra nome de arquivos dentro de pacotes 
#dentro de cada uma das pastas deve ter arquivo __init__.py
#__init__.py
#são necessários para que o Python trate diretórios contendo o arquivo como pacotes. Isso previne que diretórios com um nome comum, como string , ocultem, involuntariamente, módulos válidos que ocorrem posteriormente no caminho de busca do módulo.
'''
from package import *
No terminal, para diminuir a digitação, costuma-se importar todas as funções de math dessa forma:

from math import *
Em geral, a prática do import * de um módulo ou pacote é desaprovada, uma vez que muitas vezes dificulta a leitura do código. O uso no terminal, com dito, é muito comum.

import item.subitem.subsubitem
Em uma construção como import item.subitem.subsubitem, cada item, com exceção do último, deve ser um pacote. O último pode ser também um pacote ou módulo, mas nunca uma classe, função ou variável contida em um módulo.
'''