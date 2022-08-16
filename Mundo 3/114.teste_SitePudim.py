'''Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''

import urllib
import urllib.request
import webbrowser
url=input("Insira uma url pra saber se está acessível : ")
try:
    site=urllib.request.urlopen(url)
except:
    print(f"O site {url} não está acessível no momento")
else:
    print(f"O site {url} está acessível no momento")
    webbrowser.open(url)
