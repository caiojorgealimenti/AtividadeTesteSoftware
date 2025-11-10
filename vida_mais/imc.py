def calcular_imc(peso, altura):
    if altura <=0:
        raise ValueError("Altura deve ser maior que zero")
    return round(peso / (altura**2), 2)


def classificar_imc(imc):
    if imc <18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade Grau I"
    elif 35 <= imc < 40:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"