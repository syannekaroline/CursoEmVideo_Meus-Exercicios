'''
Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções. Aprenda como usar a estrutura try except no Python de uma forma simples.
'''

'''Exceções: Os c[odigos estão certos mas dependendo dos valores podem ocorrer exeções que geram erros: erros de atribuições - NamErro, erros de definição : NameError , erros de valores: ValueErro , ZeroDivisionErro : erro na divisão', erros de tipo : 2/'2' -  TypeErro , IndexErro - ex : referenciar uma posição não existente em uma lista , modulo não encontrado ; Módulo não encontrados'''

#TRATAR EXEÇÕES

#try : 
#   [operação]
# except: 
#   [falhou]
#else: (opcional)
#   [deu certo]
#finally:(opcional)
#   [independente se deu certo ou errado]
#há como mostrar o erro que ocorreu usando a classe printcipal de erros do python que é a Exception : except Exception as erro  ... erro.__clas s__

#um mesmo try pode ser vários try 
#pode-se testar os tipos de erro : except (ValueErro,TypeErro): 
try:
    r=(int(input("Numerado: "))/int(input("Denominador: ")))
#except:
#   print("Infelizmente tivemos um prooblema :(")

#except Exception as erro:
#    print(f"O problama encontrado foi {erro.__class__}")

except (ValueError,TypeError):
    print('Tivemos um problema com os dados que vc digitou')
except ZeroDivisionError:
    print("Não é possível realizar divisão por zero!")
except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados!")
except Exception as erro:
    print(f"A causa do erro foi : {erro.__cause__}")

else: 
    print(f"O resultado é {r}")
finally:
    print("Volte sempre! Muito Obrigada!")