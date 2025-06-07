from os import system as limp
limp("cls")

#solicitar ao usuário que insira e salve os dados em um arquivo chamado "dados_user.txt", cada vez que um usuário
#inserir dados no sistema, um valor deve ser incrementado, como um identificados do usuário (1001, 1002, 1003 .....)

import Menus
import Menus2

x = 1000
senha = 123456

Menus.menu1()

while True:

        Menus2.menu2()

        Opcao_desejada = float(input("Digite a opção desejada: "))

        if Opcao_desejada == 1:
                nome = input("Digite seu nome: ")
                data_nascimento = input("Digite sua data de nascimento: ")
                cpf = int(input("Insira seu cpf: "))
                telefone = int(input("Insira seu telefone: "))

                with open("Dados_user.txt", "a") as arquivo:
                        arquivo.write(f"ID do Usuario: {x}\nNome:{nome}\nData de Nascimento:{data_nascimento}\n\
CPF:{cpf}\nTelefone:{telefone}\n")
                x += 1

        elif Opcao_desejada == 2:
                with open("Dados_user.txt", "r") as arquivo:
                        for linha in arquivo:
                                print(linha)
        
        elif Opcao_desejada == 3:
              senha2 = float(input("INSIRA SENHA DE SEGURANÇA: "))
              if senha2 == senha:
                      with open("Dados_user.txt", "w") as arquivo:  
                       arquivo.write("")
        
        elif Opcao_desejada == 4:
               break
        

                




        
