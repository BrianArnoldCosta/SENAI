from os import system as limp
limp("cls")


def menu1():
    print(("*"*48 + "\n")*2)
    print("*"*7, end=" ")
    print("\tCALCULADORA SENAI\t", "*"*7)
    print("*"*48)

def menu2():
    print("ESCOLHA A OPÇÃO ABAIXO:\n\n1 - SOMA\n\
2 - SUBTRAÇÃO\n3 - MULTIPLICAÇÃO\n4 - DIVISÃO\n\
    \n0 - SAIR")
    
    print("*"*43, "\n\n")

def soma(x,y):
    resultado = x + y
    return resultado

def subtracao(x,y):
    resultado = x - y
    return resultado 

def multiplicacao(x,y):
    resultado = x * y
    return resultado 

def divisao(x,y):
    resultado = x / y
    return resultado 

menu1()

x = float(input("\nDigite o primeiro número que deseja cálcular: "))
y = float(input("\nDigite o segundo número que deseja calcular: "))


menu2()

while True:
    opcao_escolhida = float(input("Digite a opção desejada: "))
    if opcao_escolhida == 1:
        resultado = soma(x,y)
        print (f"O resultado é {resultado}.")
    elif opcao_escolhida == 2:
        resultado = subtracao(x,y)
        print (f"O resultado é {resultado}.")
    elif opcao_escolhida == 3:
        resultado = multiplicacao(x,y)
        print (f"O resultado é {resultado}.")
    elif opcao_escolhida == 4:
        resultado = divisao(x,y)
        print (f"O resultado é {resultado}.")
    elif opcao_escolhida == 0:
        break
    else:
        print("Selecione uma opção válida: ")


