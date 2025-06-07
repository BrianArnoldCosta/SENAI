from os import system as limp
limp("cls")

while True:
    try:
        valor1 = float(input("Digite um valor: "))
        valor2 = float(input("Digite um valor: "))

        resultado = valor1 / valor2
        print(f"Resultado do cálculo é: {resultado}")

    except ZeroDivisionError:
        limp("cls")
        print("O divisor não pode ser zero!!!")
    except ValueError:
        limp("cls")
        print("O valor inserido deve ser um número!!!")
    except:
        limp("cls")
        print("O cálculo apresentou problemas um erro desconhecido.\
\nContate o administrador do sistema")