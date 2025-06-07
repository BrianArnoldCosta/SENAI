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


# for i in range (0,51):
#         print(i)

# for i in range(0,51):
#     if i < 51:
#         print(i, end='; ')
    
# --------------------------------------------------------------------------------------------

# nome = input("Insira seu nome: ")

# for i in (nome):
#     print (i, end= ' ')

# print("\n")


# for i in (nome):
#     print(i)

# ----------------------------------------------------------------------------------------------

# nome = input("Digite uma palavra: ")

# nome = nome.upper()

# for letra in nome:
#     if letra in ['A', 'E', 'I', 'O', 'U']:
#         continue  
#     print(letra)  

# ------------------------------------------------------------------------------------------------
    
# RESOLUÇÃO PROFESSOR: 

# nome = input("Digite uma frase: ")


# for i in nome:
#     if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
#         pass
#     else:
#         print(i)


# -----------------------------------novo---------------------------------------------------
# Crie um programa em python que peça ao usuário para digitar uma frase
# Em seguida, utilizando um loop for, percorra cada palavra da frade e realize as seguintes operações:
#     1 - imprima palavra 
#     2 - conte e imprima o número de vogais presentes na frase inteira
#     3 - verifique e imprima se a palavra começa com uma vogal ou uma consoante

# frase = input("Digite uma frase: ")

# vogais = "aeiouAEIOU"

# for i in frase:
#     print(i, end= '')

# numero = 0

# for i in frase:
#     if i in vogais:
#         numero += 1

# print(f"\n\nA quantidade de vogais na frase é: {numero}")

# if frase:
#     primeira_letra = frase[0]
#     if primeira_letra in vogais:
#         print("A primeira letra é uma vogal.")
#     else:
#         print("A primeira letra não é uma vogal.")

# --------------------------------------------------------------------------------------------------
# # Crie um programa em python que peça ao usuário para digitar uma frase
# # Em seguida, utilizando um loop for, percorra cada palavra da frade e realize as seguintes operações:
# #     1 - imprima palavra SEPARADAMENTE
# #     2 - conte e imprima o número de vogais presentes na frase inteira
# #     3 - verifique e imprima se a palavra começa com uma vogal ou uma consoante

frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"
palavras = frase.split()


for i in palavras:
    print(f"\n {palavras}" )

numero = 0

for i in palavras:
    if i in vogais:
        numero += 1

print(f"\n\nA quantidade de vogais na frase é: {numero}")

if palavras:
    primeira_letra = frase[0]
    if primeira_letra in vogais:
        print("A primeira letra é uma vogal.")
    else:
        print("A primeira letra não é uma vogal.")





























# ---------------------------------------------------------------------------------------------------------------------------
# # Programa que analisa uma frase digitada pelo usuário

# # Solicita ao usuário que digite uma frase
# frase = input("Digite uma frase: ")

# # Divide a frase em palavras
# palavras = frase.split()

# # Inicializa o contador de vogais
# contador_vogais = 0

# # Define as vogais (incluindo maiúsculas)
# vogais = "aeiouAEIOU"

# # Loop para percorrer cada palavra da frase
# for palavra in palavras:
#     print(f"\nPalavra: {palavra}")
    
#     # Verifica se a palavra começa com vogal ou consoante
#     if palavra[0] in vogais:
#         print("→ Começa com uma vogal.")
#     else:
#         print("→ Começa com uma consoante.")
    
#     # Conta as vogais na palavra
#     for letra in palavra:
#         if letra in vogais:
#             contador_vogais += 1

# # Exibe o número total de vogais na frase
# print(f"\nNúmero total de vogais na frase: {contador_vogais}")
