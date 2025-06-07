from os import system as limp
limp("cls")

# def teste():
#     print ("Minha primeira função !!!")
#     return None

# def par(nome,idade):
#     print(f"Você é {nome} e tem {idade} anos ?")

# print("Bem vindo ao SENAI !!!!")

# teste()
# par("Luiz",21)

def soma(x,y):
    resultado = x + y
    return resultado

print ("Bem vindo à calculadora SENAI.\
       Insira os números que deseja calcular")

x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

valor = soma(x,y)

print (f"O resultado é {valor}.")

def subtracao(x,y):
    resultado = x - y
    return resultado 


valor = subtracao(x,y)

print (f"O resultado é {valor}.")

def multiplicacao(x,y):
    resultado = x * y
    return resultado 


valor = multiplicacao(x,y)

print (f"O resultado é {valor}.")

def divisao(x,y):
    resultado = x / y
    return resultado 


valor = divisao(x,y)

print (f"O resultado é {valor}.")

