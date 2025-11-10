def calcular_eficiencia(potencia_saida, potencia_entrada):
    if potencia_entrada <= 0:
        raise ValueError("Potência de entrada deve ser maior que zero.")
    eficiencia = (potencia_saida / potencia_entrada) * 100
    return round(eficiencia, 2)

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
    return {
        "potencia_saida": potencia_saida,
        "potencia_entrada": potencia_entrada,
        "eficiencia": eficiencia,
        "classificacao": classificacao,
    }