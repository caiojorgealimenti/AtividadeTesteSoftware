import pytest
from eficiencia_motor import calcular_eficiencia, classificar_eficiencia, analise_motor

def test_calculo_eficiencia_90():
    assert calcular_eficiencia(900, 1000) == 90.0

def test_calculo_eficiencia_85_5():
    assert calcular_eficiencia(855, 1000) == 85.5

def test_potencia_entrada_zero():
    with pytest.raises(ValueError):
        calcular_eficiencia(800, 0)

def test_classificacao_IE1():
    assert classificar_eficiencia(75.0) == "IE1 - Baixa eficiência"

def test_classificacao_IE2():
    assert classificar_eficiencia(85.0) == "IE2 - Eficiência média"

def test_classificacao_IE3():
    assert classificar_eficiencia(92.0) == "IE3 - Alta eficiência"

def test_integracao_analise_motor():
    eficiencia, classe = analise_motor(880, 1000)
    assert eficiencia == 88.0
    assert classe == "IE2 - Eficiência média"