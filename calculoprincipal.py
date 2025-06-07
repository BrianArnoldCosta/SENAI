from os import system as limp
limp("cls")

import menus
import menu2
import calculadora as calc

menus.menu1()

menu2.menu2()

while True:
    opcao_escolhida = float(input("Digite a opção desejada: "))

    x = float(input("\nDigite o primeiro número que deseja cálcular: "))
    y = float(input("\nDigite o segundo número que deseja calcular: "))

    if opcao_escolhida == 1:
        resultado = calc.soma(x,y)
        print (f"O resultado é {resultado}.")
    elif opcao_escolhida == 2:
        resultado = calc.subtracao(x,y)
        print (f"O resultado é {resultado}.")
    elif opcao_escolhida == 3:
        resultado = calc.multiplicacao(x,y)
        print (f"O resultado é {resultado}.")
    elif opcao_escolhida == 4:
        resultado = calc.divisao(x,y)
        print (f"O resultado é {resultado}.")
    elif opcao_escolhida == 5:
        resultado = calc.exponenciacao(x,y)
        print (f"O resultado é {resultado}.")
    elif opcao_escolhida == 6:
        resultado = calc.raiz_quadrada(x,y)
        print (f"O resultado é {resultado}.")
    elif opcao_escolhida == 7:
        resultado = calc.seno(x,y)
        print (f"O resultado é {resultado}.")
    elif opcao_escolhida == 8:
        resultado = calc.cosseno(x,y)
        print (f"O resultado é {resultado}.")
    elif opcao_escolhida == 0:
        break
    else:
        print("Selecione uma opção válida: ")
