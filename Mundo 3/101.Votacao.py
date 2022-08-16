'''
Exercício Python 101: Crie um programa que tenha uma 
função chamada voto() que vai receber como parâmetro o 
ano de nascimento de uma pessoa, retornando um valor 
literal indicando se uma pessoa tem voto NEGADO, 
OPCIONAL e OBRIGATÓRIO nas eleições.
'''
def voto(nasc):
    from datetime import date
    idade=date.today().year-nasc
    if idade <16:
        resp="Voto Negado"
    elif (idade>=16 and idade<18) or idade >70 :
        resp="Voto Opcional"
    else :
        resp="Voto obrigatório"    
    return f"Para {idade} anos : {resp}"

print(voto(int(input("Insira o ano de nascimento:  "))))