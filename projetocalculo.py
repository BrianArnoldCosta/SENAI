from os import system as limp   
limp("cls")

valor1 = float(input("DIGITE O PRIMEIRO VALOR: "))
valor2 = float(input("DIGITE O SEGUNDO VALOR: "))
soma = None
sub = None
mult = None
div = None
exp = None


soma = valor1 + valor2
sub = valor1 - valor2
mult = valor1 * valor2
div = valor1 / valor2
exp = valor1 ** valor2


print(f"A SOMA DE VALOR1 COM VALOR 2 É: {soma}\
\nA SUBTRAÇÃO DE VALOR1 COM VALOR 2 É: {sub}\
\nA MULTIPLICAÇÃO DE VALOR1 COM VALOR 2 É: {mult}\
\nA DIVISÃO DE VALOR1 COM VALOR 2 É: {div}\
\nE A EXPONENCIAÇÃO DE VALOR1 COM VALOR 2 É:{exp}")


