def verifica_numero(num):
    if num % 2 == 0:
        print("Esse número é par!")
    else:
        print("Esse número é ímpar")

numero= int(input("Digite um número: "))
verifica_numero(numero)