temperatura_celsius = int(input("Digite a temperatura em graus celsius: "))
def celsius_fahrenheit(temp_celsius):
    temp_fahrenheit = (temp_celsius * 9 / 5) + 32
    return temp_fahrenheit
temperatura_fahrenheit= celsius_fahrenheit(temperatura_celsius)
print(temperatura_celsius, "°C equivalem a : ", temperatura_fahrenheit, "°F")
