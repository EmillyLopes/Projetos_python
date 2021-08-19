def retorna_soma(valores):
    soma = 0
    for valor in valores:
        soma = soma + valor

    return soma

numeros = [5, 10, 15, 25]

soma_numeros= retorna_soma(numeros)
print(soma_numeros)