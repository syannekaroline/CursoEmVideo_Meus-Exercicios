'''Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

def leiaInt():
    while True:
        try:
            n=int(input("\nInsira o um número inteiro: "))
        except KeyboardInterrupt:
            print("O suário preferiu não inserir o valor ")
            n=0
        except:
            print("\n\033[31m ERRO! digite um número inteiro válido.\033[m")
        else:
            return n

def leiafloat():
    while True:
        try:
            n=float(input("\nInsira o um número real: "))
        except KeyboardInterrupt:
            print("O suário preferiu não inserir o valor ")
            n=0
        except:
            print("\n\033[31m ERRO! digite um número flutuante válido.\033[m") 
        else:
            return n


inteiro=leiaInt()
float=leiafloat()

print(f"O valor inteiro inserido foi {inteiro} e o valor real inserido foi {float}")

