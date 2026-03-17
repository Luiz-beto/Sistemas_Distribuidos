"""Testes unitários do módulo calculadora."""
import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from calculator import add, subtract, multiply, divide


def test_soma():
    """Soma de dois números."""
    assert add(2, 3) == 5


def test_subtracao():
    """Subtração de dois números."""
    assert subtract(5, 3) == 2


def test_multiplicacao():
    """Multiplicação de dois números."""
    assert multiply(3, 4) == 12


def test_divisao():
    """Divisão e erro ao dividir por zero."""
    assert divide(10, 2) == 5
    with pytest.raises(ValueError, match="dividir por zero"):
        divide(1, 0)
