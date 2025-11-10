import pytest
from industria.eficiencia_motor import calcular_eficiencia, classificar_eficiencia, analise_motor

def test_calcular_eficiencia_900_1000():
    assert calcular_eficiencia(900, 1000) == 90.0

def test_calcular_eficiencia_855_1000():
    assert calcular_eficiencia(855, 1000) == 85.5

def test_calcular_eficiencia_entrada_zero():
    with pytest.raises(ValueError):
        calcular_eficiencia(800, 0)

def test_classificar_eficiencia_baixa():
    assert classificar_eficiencia(75.0) == "IE1 - Baixa eficiência"

def test_classificar_eficiencia_media():
    assert classificar_eficiencia(85.0) == "IE2 - Eficiência média"

def test_classificar_eficiencia_alta():
    assert classificar_eficiencia(92.0) == "IE3 - Alta eficiência"

def test_analise_motor_integracao():
    resultado = analise_motor(880, 1000)
    assert resultado["eficiencia"] == 88.0
    assert resultado["classificacao"] == "IE2 - Eficiência média"
