# Conversão de temperatura Celsius para Fahrenheit
def converterCelsius_Fahrenheit(temperatura):
    conversao = (temperatura * 1.8) + 32
    return conversao

temperatura = float(input("Digite os graus em Celsius aqui: "))
resultado = converterCelsius_Fahrenheit(temperatura)
print(f"A conversão de {temperatura} ºC para Fahrenheit é: {resultado}")

# Conversão de temperatura Fahrenheit para Celsius
def converterFahrenheit_Celsius(temperaturaFahrenheit):
    conversao2 = (temperaturaFahrenheit - 32) / 1.8
    return conversao2

temperaturaFahrenheit = float(input("Digite os graus em Fahrenheit aqui: "))
resultado2 = converterFahrenheit_Celsius(temperaturaFahrenheit)
print(f"A conversão de {temperaturaFahrenheit} ºF para Celsius é: {resultado2}")