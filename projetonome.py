from os import system as limp 
limp("cls")

# nome = input("Digite seu nome:")
# print(nome)

# ano = 2025
# data = int(input("Digite o ano que você nasceu: "))
# idade = ano - data
# print("Sua idade é:",idade,"anos.")


#SOLICITAR AO USUÁRIO QUE INSIRA OS DADOS NA TELA DO SISTEMA: 
#NOME: DEVE SER UMA STRING
#DATA NASCIMENTO: DEVE SER UMA STRING
#CPF: DEVE SER UMA INT
#TELEFONE: DEVE SER UMA INT

#APÓS GERAL UMA FUNÇÃO PRINT QUE TRAGA TODAS AS INFORMAÇÕES DE FORMA ORGANIZADA

nome = input("Digite seu nome: ")
nasc = input("Digite a data do seu nascimento: ")
cpf = int(input("Digite seu CPF: "))
tel = int(input("Digite seu telefone: "))

print("\n\nMEUS DADOS SÃO:\n\nNOME:",nome,"\nDATA DE NASCIMENTO:",nasc,"nCPF",cpf,"\nTELEFONE:",tel,sep="")

limp("cls")
print("SEUS DADOS SÃO:\n\nNOME:",nome,"\nDATA DE NASCIMENTO:",nasc,"nCPF",cpf,"\nTELEFONE:",tel,sep="")
print("PRESSIONE ENTER PARA ")
