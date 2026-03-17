"""Módulo de calculadora simples."""


def add(a: float, b: float) -> float:
    """Soma dois números."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtrai o segundo número do primeiro."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiplica dois números."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide o primeiro pelo segundo. Erro se o divisor for zero."""
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b
