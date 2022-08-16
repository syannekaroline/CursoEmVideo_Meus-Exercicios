import re
def cabecalho(msg,color=30):
    print("-="*30)
    print(f"\033[{str(color)}m{msg.upper():^60}\033[m")
    print("-="*30)

def ArquivoExiste(arquivo):
    try:
        r=open(arquivo,'rt')   
    except FileNotFoundError:
        return False
    else:
        return True


def criar_txt(arquivoName):

    try: 
        arquivo = open(arquivoName, 'wt+')
        arquivo.close()
    except:
        print("Erro na criação do arquivo")
    else:
        print("Arquivo Exercício105.txt Criado com sucesso!")

def cadastrar_txt(arquivoName,nome='desconhecido',idade=0):
    try:
        arquivo=open(arquivoName,'at')
    except:
        print("houve um erro na abertura do arquivo")
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print("Houve um erro no cadastro de dados!")
        else:
            print("Novo registo add com sucesso!!")
            arquivo.close()


def ler_txt(arquivo):
    try: 
        arquivo = open(arquivo, 'rt')
    except:
        print("Falha ao ler arquivo :(")
    else:
        cabecalho("pessoas cadastradas")
        print(f"\033[35m{'Nome':^30}|\033[36m{'Idade':^30}\033[m")
        for item in arquivo.readlines():
            idade=re.sub(r'\D',"",item.replace(";",""))
            nome=re.sub(r"\d","",item.replace(";","")).replace("\n","")
            print(f'\033[33m{nome:^30}\033[m|\033[34m{idade:^30}\033[m')
            
        arquivo.close()

