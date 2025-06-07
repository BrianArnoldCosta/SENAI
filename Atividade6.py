# #CRIE UMA FUNÇÃO CALCULADORA (NUM1,NUM2,OPERAÇÃO) QUE RECEBA DOIS NÚMEROS E 
# #UMA STRING DE OPERAÇÃO (+,-. *, /). A FUNÇÃO DEVE: 

# #1 - TENTAR CONVERTER NUM1 E NUM2 PARA FLOAT. SE VALUEERROR OCORRER, IMPRIMIR"ERRO: ENTRADA NÚMERICAS INVÁLIDAS" E RETORNAR NONE.
# 2 - REALIZAR A OPERAÇÃO ESPECIFICADA.
# 3 - SE A OPERAÇÃO FOR / E NUM2 FOR ZERO(APÓS CONVERSÃO), TRATAR ZeroDivisionError IMPRIMINDO "ERRO:DIVISÃO POR ZERO" E RETORNANDO NONE.
# 4 - SE A OPERAÇÃO NÃO FOR UMA DAS ESPERADAS, IMPRIMIR "ERRO: OPERAÇÃO INVÁLIDA."E RETORNAR NONE.
# 5 - SE TUDO OCORRER BEM, RETORNAR O RESULTADO.

# from os import system as limp
# limp("cls")

# import menus
# import Operacoes as oper

# menus.menu1()
# while True:
#     try:
#         num1 = input("Digite o valor do primeiro número: ")
#         num1_float = float(num1)
#         num2 = input("Digite o valor do primeiro número: ")
#         num2_float = float(num2)

#     except ValueError:
#         limp("cls")
#         print("ERRO: ENTRADAS NUMÉRICAS INVÁLIDAS.!!!")
    
#     operacao = input("Insira operação desejada: ")

#     if operacao == "+":
#             resultado = oper.soma(num1_float,num2_float)
#             print(f"CÁLCULO REALIZADO COM SUCESSO")
#             print (f"\n\nO resultado é {resultado}.")
#     elif operacao == "-":
#             resultado = oper.subtracao(num1_float,num2_float)
#             print(f"CÁLCULO REALIZADO COM SUCESSO")
#             print (f"\n\nO resultado é {resultado}.")
#     elif operacao == "*":
#             resultado = oper.multiplicacao(num1_float,num2_float)
#             print(f"CÁLCULO REALIZADO COM SUCESSO")
#             print (f"\n\nO resultado é {resultado}.")
#     elif operacao == "/":
#         try: 
#             resultado = oper.divisao(num1_float,num2_float)
#             print(f"CÁLCULO REALIZADO COM SUCESSO")
#             print (f"\n\nO resultado é {resultado}.")
#         except ZeroDivisionError: 
#             limp("cls")
#             print("ERRO: DIVISÃO POR ZERO!!!")
            
#     else:
#         print("ERRO: OPERAÇÃO INVÁLIDA.")


x = 1
x = x == x