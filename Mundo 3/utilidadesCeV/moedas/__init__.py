from curses.ascii import isdigit

def aumentar(float,percent,format=False):
    '''Função que recebe como parâmetro um valor flutuante e um valor em percentagem, retornando o aumento dessa porcentagem em cima do valor recebido'''
    res= float+float*(percent/100) if format==False else moeda(float+float*(percent/100))
    return res

def diminuir(float,percent,format=False):
    '''Função que recebe como parâmetro um valor flutuante e um valor em percentagem, retornando a redução dessa porcentagem em cima do valor recebido'''
    res= float-float*(percent/100) if format==False else moeda(float-float*(percent/100))
    return res

    
def dobro (valor,format=False):
    '''Função que recebe um valor e retorna seu dobro'''
    res= valor*2  if format==False else moeda(valor*2)
    return res


def metade (valor,format=False):
    '''Função que recebe um valor e retorna sua metade, se ele for numérico'''
    res= valor/2  if format==False else moeda(valor/2 )
    return res

def moeda( valor,moeda='R$'):
    return f'{moeda}{valor:^.2f}'.replace('.',',')

def cabecalho(msg):
    print("-="*30)
    print(f"{msg.upper():^60}")
    print("-="*30)

def resumo (valor):
    cabecalho('Resumo do valor')
    print(f"|Preço analisado   : {moeda(valor):>40}")
    print(f"|Aumento de 10%    : {(aumentar(valor,10,format=True)):>40}")
    print(f"|Diminuição de 10% : {diminuir(valor,10,format=True):>40}")
    print(f"|O dobro :           {dobro(valor,format=True):>40}")
    print(f"|A metade :          {metade(valor,format=True):>40}")