from curses.ascii import isalnum


def leiaDinheiro(msg):
    
    while True :
        numero=(input(f"{msg}").strip()).replace(",",".")
        if numero.replace(".","").isnumeric():
            break
        else:
            print(f'\033[1;31mERRO : "{numero}" é um preço inválido\033[m')
    return float(numero)
