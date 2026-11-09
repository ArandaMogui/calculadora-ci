from calculadora import restar, sumar
import calculadora

def test_sumar():
    assert calculadora.sumar(2, 3) == 5

def test_restar():
    assert calculadora.restar(5, 3) == 2
    