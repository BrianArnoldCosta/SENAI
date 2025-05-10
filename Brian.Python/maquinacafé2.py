from os import system as limp
limp("cls")

# print(("*"*43 + "\n")*3)
# print("*"*10,end="")
# print("\tCAFÉ'S SENAI\t","*"*10)
# print("*"*43)
# print("ESCOLHA UMA BEBIDA ABAIXO:\n\n1 - CAFÉ EXPRESSO\n\
# 2 - CAFÉ COM LEITE\n3 - CAPPUCCINO\n4 - ÁGUA QUENTE\n\
# 5 - LEITE PURO")

# print("*"*43,"\n\n")


# opcao = float(input("DIGITE A OPÇÃO DESEJADA: "))
# texto = "APRECIE SEU"

# bebidas = {
#     1: "CAFÉ EXPRESSO",
#     2: "CAFÉ COM LEITE",
#     3: "CAPPUCCINO",
#     4: "ÁGUA QUENTE",
#     5: "LEITE PURO",
#     75452: "MANUTENÇÃO DA MÁQUINA"
# }

# mensagem = bebidas.get(opcao)

# if mensagem:
#     if opcao == 75452:
#         print(mensagem)
#     else:
#         print(texto, mensagem)
# else:
#     print("ERRO, OPÇÃO INVÁLIDA")
    

# while True:
#     print(("*"*43 + "\n")*3)
#     print("*"*10, end="")
#     print("\tCAFÉ'S SENAI\t", "*"*10)
#     print("*"*43)
#     print("ESCOLHA UMA BEBIDA ABAIXO:\n\n1 - CAFÉ EXPRESSO\n\
# 2 - CAFÉ COM LEITE\n3 - CAPPUCCINO\n4 - ÁGUA QUENTE\n\
# 5 - LEITE PURO\n0 - SAIR")

#     print("*"*43, "\n\n")

#     try:
#         opcao = float(input("DIGITE A OPÇÃO DESEJADA: "))
#         texto = "APRECIE SEU"

#         bebidas = {
#             1: "CAFÉ EXPRESSO",
#             2: "CAFÉ COM LEITE",
#             3: "CAPPUCCINO",
#             4: "ÁGUA QUENTE",
#             5: "LEITE PURO",
#             75452: "MANUTENÇÃO DA MÁQUINA"
#         }

#         if opcao == 0:
#             print("OBRIGADO POR UTILIZAR A MÁQUINA. VOLTE SEMPRE!")
#             break

#         mensagem = bebidas.get(opcao)

#         if mensagem:
#             if opcao == 75452:
#                 print(mensagem)
#             else:
#                 print(texto, mensagem)
#         else:
#             print("ERRO, OPÇÃO INVÁLIDA")

#     except ValueError:
#         print("POR FAVOR, DIGITE UM NÚMERO VÁLIDO.")

# import time
# import os  # Usado para limpar a tela

# def limpar_tela():
#     # Limpa a tela dependendo do sistema operacional
#     os.system('cls' if os.name == 'nt' else 'clear')

# while True:
#     limpar_tela()
#     print(("*"*43 + "\n")*3)
#     print("*"*10, end="")
#     print("\tCAFÉ'S SENAI\t", "*"*10)
#     print("*"*43)
#     print("ESCOLHA UMA BEBIDA ABAIXO:\n\n1 - CAFÉ EXPRESSO\n\
# 2 - CAFÉ COM LEITE\n3 - CAPPUCCINO\n4 - ÁGUA QUENTE\n\
# 5 - LEITE PURO\n0 - SAIR")

#     print("*"*43, "\n\n")

#     try:
#         opcao = float(input("DIGITE A OPÇÃO DESEJADA: "))
#         texto = "APRECIE SEU"

#         bebidas = {
#             1: "CAFÉ EXPRESSO",
#             2: "CAFÉ COM LEITE",
#             3: "CAPPUCCINO",
#             4: "ÁGUA QUENTE",
#             5: "LEITE PURO",
#             75452: "MANUTENÇÃO DA MÁQUINA"
#         }

#         if opcao == 0:
#             print("OBRIGADO POR UTILIZAR A MÁQUINA. VOLTE SEMPRE!")
#             break

#         mensagem = bebidas.get(opcao)

#         if mensagem:
#             if opcao == 75452:
#                 print("A máquina está em manutenção.")
#             else:
#                 print(f"\n{texto} {mensagem}")
#                 print("Preparando sua bebida", end="", flush=True)
#                 for _ in range(5):
#                     time.sleep(1)
#                     print(".", end="", flush=True)
#                 print("\nBebida pronta! Aproveite!\n")
#         else:
#             print("ERRO, OPÇÃO INVÁLIDA")

#         time.sleep(5)

#     except ValueError:
#         print("POR FAVOR, DIGITE UM NÚMERO VÁLIDO.")
#         time.sleep(2)



# valor1 = float(input("Insira o primeiro valor: "))
# valor2 = float(input("Insira o primeiro valor: "))

# if valor1 == valor2:
#     print("VALORES NÃO PODEM SER IGUAIS, INSERIR VALORES DIFERENTES")

# elif valor1 > valor2 or valor2 > valor1: 
#     print("ESTE É O MAIOR ENTRE ELES")

# else:
#     "PROGRAMA FINALIZADO"


# #PROGRAMA PERSONALIZADO COM GPT
# valor1 = float(input("Insira o primeiro valor: ").replace(',', '.'))
# valor2 = float(input("Insira o primeiro valor: ").replace(',', '.'))

# if valor1 == valor2:
#     print("VALORES NÃO PODEM SER IGUAIS, INSERIR VALORES DIFERENTES")

# else:
#     valor_maior = max(valor1, valor2)
#     print(valor_maior, "É O MAIOR ENTRE ELES")


# idade = float(input("INSIRA SUA IDADE: "))
# texto = "VOCÊ SE ENCAIXA NO GRUPO DE:"

# if idade >=0 and idade <=12:
#     print (texto,"CRIANÇAS")

# elif idade >=13 and idade <=17:
#     print(texto,"ADOLESCENTE")

# elif idade >=18 and idade <=59:
#     print(texto,"ADULTO")

# elif idade >=60:
#     print(texto,"IDOSO")

# elif idade <0:
#     print ("ERRO, NÃO EXISTE IDADE NEGATIVO")

nota_final = float(input("DIGITE O VALOR DA NOTA FINAL DO ALUNO: "))
frequencia = float(input("DIGITE O VALOR DA FREQUÊNCIA DO ALUNO: "))

if 7 <= nota_final <= 10 and frequencia>=75:
    print("ALUNO FOI APROVADO") 

elif nota_final >=11:
    print("NOTA MÁXIMO É 10, CORRIGIR")

elif frequencia>=101:
    print("FREQUÊNCIA 100%, FAVOR CORRIGIR")

elif nota_final <0 or frequencia <0:
    print("NÃO EXISTE VALOR NEGATIVO, CORRIGIR")

else: 
    print("O ALUNO ESTÁ REPROVADO")

