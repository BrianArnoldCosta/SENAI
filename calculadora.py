def soma(numero1,numero2):
    res = numero1 + numero2
    return res

def sub( numero1, numero2):
    res = numero1 - numero2
    return res

def div(val1, val2):
    try:
        res = val1 / val2
        return res
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero!")
        return None

def mult(num1, num2):
    result = num1 * num2
    return result

def raiz (numero1, numero2):
    res = numero1 ** (1/numero2)
    return res

def expoente(valor1, valor2):
    resultado = valor1 ** valor2
    return resultado

import math
def calcular_seno(valor):
    """Calcula o seno de um ângulo em radianos."""
    return math.sin(valor)
def calcular_cosseno(valor):
    """Calcula o cosseno de um ângulo em radianos."""
    return math.cos(valor)
def calcular_tangente(valor):
    """Calcula a tangente de um ângulo em radianos."""
    return math.tan(valor)