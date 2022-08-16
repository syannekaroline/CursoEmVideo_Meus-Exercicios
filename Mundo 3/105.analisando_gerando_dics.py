'''
Exercício Python 105: Faça um programa que tenha uma função 
notas() que pode receber várias notas de alunos e vai retornar 
um dicionário com as seguintes informações:
– Quantidade de notas                                                                                                                                                  
– A maior nota                                                                                                                                                                
– A menor nota                                                                                                                                                              
– A média da turma                                                                                                                                                     
– A situação (opcional)
'''

def notas(*notas,sit='N'):
    resul=dict()
    print(notas)
    resul['quantidade']=len(notas[0])
    resul['A maior nota']=max(notas[0])
    resul['A menor nota']=min(notas[0])
    resul['Média']=sum(notas[0])/len(notas[0])
    if sit=='S':
        if resul['Média']<=5:
            resul["situação"]="Ruim"
        elif resul['Média']>5 and resul['Média']<=7:
            resul["situação"]="Mediana"
        elif resul['Média']>7 and resul['Média']<=8:
            resul["situação"]="boa"
        else:
            resul["situação"]="Exelente"
    return resul
resultado=notas(tuple(map(int,input("Insira as notas separadas por espaço: ").split())),sit=input("Deseja analisar a situação [s/n] : ").upper())
print(resultado)