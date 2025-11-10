import pytest
from imc import calcular_imc, classificar_imc

def test_calcular_imc_valor_especifico():
    assert calcular_imc(70, 1.75) == 22.86

def test_calcular_imc_arredondamento():
    assert calcular_imc(70, 1.75) == 22.86
    assert calcular_imc(80, 1.80) == 24.69

def test_calcular_imc_altura_zero_gera_erro():
    with pytest.raises(ValueError):
        calcular_imc(70, 0)

@pytest.mark.parametrize("imc_valor, classificacao_esperada", [
    (17.9, "Abaixo do peso"),
    (22.0, "Peso normal"),
    (27.3, "Sobrepeso"),
    (33.0, "Obesidade grau I"),
    (37.0, "Obesidade grau II"),
    (45.0, "Obesidade grau III"),
])
def test_classificar_imc_varios_casos(imc_valor, classificacao_esperada):
    assert classificar_imc(imc_valor) == classificacao_esperada