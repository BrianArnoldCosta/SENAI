def somar(a, b):
    """Soma dois números e retorna o resultado."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ambas as entradas devem ser números")
    return a + b

def subtrair(a,b):
    return a - b

def dividir(a,b):
    if b == 0:
        raise ZeroDivisionError("Erro: Divisão por zero!")
    return a / b