def operacoes(num_1, num_2):
    soma =num_1 + num_2
    subtracao = num_1 - num_2
    multiplicacao= num_1 * num_2
    divisao = num_1 / num_2

    print("Soma: " + str(soma))
    print("Subtração: " + str(subtracao))
    print("Multiplicação: " + str(multiplicacao))
    print("Divisão: " + str(divisao))

numero_1 = int(input("Informe o primeiro número: "))
numero_2 = int(input("Informe o segundo número: "))
operacoes(numero_1,numero_2)