def cabecalho(msg,color=30):
    print("-="*30)
    print(f"\033[{str(color)}m{msg.upper():^60}\033[m")
    print("-="*30)

def leiaInt(msg):
    while True:
        try:
            n=int(input(f"\n{msg}"))
        except KeyboardInterrupt:
            print("O suário preferiu não inserir o valor ")
            n=0
        except:
            print("\n\033[31m ERRO! digite um número inteiro válido.\033[m")
        else:
            return n

def menu(list):
    print(f"\033[35m{'Opção':^30}|\033[36m{'Operação':^30}\033[m")
    for i,item in enumerate(list): 
        print(f'\033[33m{i+1:^30}\033[m|\033[34m{item:^30}\033[m')
    op=leiaInt("Digite a opção desejada: ")
    return op

def Interface(cabecalhoMsg,MenuList):

    cabecalho(cabecalhoMsg,33)
    op=menu(MenuList)
    cabecalho(MenuList[op-1],36)

    return op
    
