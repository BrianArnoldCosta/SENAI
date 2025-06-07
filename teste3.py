from os import system as limp
limp("cls")

import calculadora


while True:

            operacao = float(input("Digite a opção escolhida: "))
            valor1 = float(input("Digite a opção escolhida: "))
            valor2 = float(input("Digite a opção escolhida: "))

            if operacao == 0:
                print("Opção SAIR Selecionada.")
                break
            if operacao == 1:
                print("Opção Soma Selecionada.")
                valor = calculadora.soma(valor1, valor2)


            elif operacao == 2:
                print("Opção Subtração Selecionada.")
                valor = calculadora.sub(valor1, valor2)


            elif operacao == 3:
                print("Opção Multiplicação Selecionada.")
                valor = calculadora.mult(valor1, valor2)


            elif operacao == 4:
                print("Opção Divisão Selecionada.")
                valor = calculadora.div(valor1, valor2)
                if valor is None:
                    continue
        
            elif operacao == 5:
                print("Opção Exponenciação Selecionada.")
                valor = calculadora.expoente(valor1, valor2)


            elif operacao == 6:
                print("Opção Raiz Selecionada.")
                valor = calculadora.raiz(valor1)
                if valor is None:
                    continue


            elif operacao == 7:
                print("Opção Seno Selecionada.")
                valor = calculadora.calcular_seno(valor1)


            elif operacao == 8:
                print("Opção Cosseno Selecionada.")

            print("Cálculo Realizado Com Sucesso!!")
            print(f"Resultado da operação: {valor}\n")