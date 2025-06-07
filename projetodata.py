#CRIAR UM SISTEMA QUE SOLICITE AO USUÁRIO QUE INSIRA SEUS DADOS: 
#NOME, DIA DE NASCIMENTO, MES DE NASCIMENTO (DEVE SER UM NÚMERO), ANO DE NASCIMENTO
#IMPRIMIR A SEGUINTE INFORMAÇÕA APÓS O USUÁRIO INSERIR SEUS DOADOS : 

#BEM VINDO <NOME> AO SENAI!!!!
#SUA DATA DE NASCIMENTO É <DIA>/<MES>/<ANO>.

from os import system as limp 
limp("cls")

#Realizado por Brian
# nome = input("Digite seu nome: ")
# dia_nasc = input("Digite o dia seu nascimento: ")
# mes_nasc = input("Digite o mês do seu nascimento: ")
# ano_nacs = int(input("Digite o ano do seu nascimento: "))
# idade = 2025 - ano_nacs

# input("\nTecle enter para continuar.....\n")

# print(f"Bem vindo",nome,"ao SENAI !!!\n")
# print("Sua data de nascimento é ",dia_nasc,"/",mes_nasc,"/",ano_nacs," ?",sep="")
# print("Sua idade atual é",idade,"anos ?")


#REALIZADO PELO PROFESSOR
nome = input("Digite seu nome: ")
dia= input("Digite o dia seu nascimento: ")
mes = input("Digite o mês do seu nascimento: ")
ano = int(input("Digite o ano do seu nascimento: "))
idade = 2025 - ano

input("\nTecle enter para continuar.....\n")

print(f"Bem vindo {nome} ao SENAI !!!",end="")
print(f"\nSua data de nascimento é {dia}/{mes}/{ano}?",sep="")
print(f"Sua idade atual é {idade} anos ?")