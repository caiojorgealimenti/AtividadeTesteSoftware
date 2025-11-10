def calcular_eficiencia(potencia_saida, potencia_entrada):
    if potencia_entrada == 0:
        raise ValueError("A potência de entrada não pode ser zero.")
    eficiencia = (potencia_saida / potencia_entrada) * 100
    return round(eficiencia, 1)


def classificar_eficiencia(eficiencia):
    if eficiencia < 80:
        return "IE1 - Baixa eficiência"
    elif eficiencia < 90:
        return "IE2 - Eficiência média"
    else:
        return "IE3 - Alta eficiência"


def analise_motor(potencia_saida, potencia_entrada):
    eficiencia = calcular_eficiencia(potencia_saida, potencia_entrada)
    classificacao = classificar_eficiencia(eficiencia)
    return eficiencia, classificacao