from os import system as limp
limp("cls")
# -----------------------------------------------------------------------------------
# pessoas = 10

# while pessoas > 0:
#     print(f"Contagem de pessoas: {pessoas}")
#     pessoas -=1


# senha = 123

# usuario= float(input("Insira a sua senha: "))

# while usuario != senha:
#     usuario=float(input("Senha errada, digite novamente: "))
# print("VAI CORINTHIANS !")

# -----------------------------------------------------------------------------------
# while True:

#     numero = int(input("Digite um número para ver sua tabuada do número: "))

#     x = 1

#     while x <= 10:
#         print(f"{numero} x {x} = {numero * x}")
#         x += 1  
    
#     if numero == 999:
#         print ("Até mais e VAI CORINTHIANS!!!")
#         break
# ---------------------------------------------------------------------------------

# for x in range (11):
#     print(f"Valor de x: {x}")

# -------------------------------------------------------------------------------
# i = 0  

# while True:
#     numero = int(input("Digite um número: "))

#     if numero % 2 == 0:
#         print(f"{numero} é par")
#         i += 1
#     else:
#         print(f"{numero} é ímpar")
#         i = 0  

#     if i == 3:
#         print("Foram digitados 3 números pares seguidos. Até breve e VAI CORINTHIANS!!!")
#         break


# -----------------------------------------------------------------------------------

# for i in range(0, 101):
#     if i % 10 == 0:
#         print(f"Os números múltiplos são: {i}")

# -------------------------------------------------------------------------------------

valor = int(input("Digite um valor: "))

for i in range (valor + 1):
    if i % 10 == 0 and i > 0:
        print(i)