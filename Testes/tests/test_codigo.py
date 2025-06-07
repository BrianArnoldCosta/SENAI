from minhas_funcoes import somar, subtrair, dividir
import pytest

def test_soma_positiva():
    """Verifica se a soma de dois números positivos está correta."""
    assert somar(5, 3) == 8

def test_soma_com_negativo():
    """Verifica a soma com um número negativo."""
    assert somar(10, -2) == 8

def test_subtracao():
    """Verifica uma subtração simples."""
    assert subtrair(10, 5) == 5

def test_divisao():
    """Verifica uma subtração simples."""
    assert dividir(10, 5) == 2

def test_soma_com_tipo_invalido():
    """Verifica se a função levanta um erro ao receber um tipo inválido."""
    with pytest.raises(TypeError):
        somar(5, "texto")

