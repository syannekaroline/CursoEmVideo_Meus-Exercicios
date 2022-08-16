'''
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. 
'''

def escreva(msg):
    n=len(msg)+4
    print('='*n)
    print('  {}'.format(msg))
    print('='*n)

escreva('syanne')
escreva('syanne karoline moreira tavares')