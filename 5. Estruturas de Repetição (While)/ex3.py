
## 3. Conversor de Temperatura: Faça um programa que receba uma temperatura em Celsius e converta para Fahrenheit. Repita o programa até o usuário digitar 0. Quando isso acontecer, mostre uma mensagem de saída

#b Iniciando a variável celsius com -1 para que passe na condição while
celsius = -1

#b Enquanto a variável celsius for diferente de zero ...
while celsius != 0:
    #b ... solicite uma nova temperatura
    celsius = float(input("Digite uma temperatura em Celcius: "))
    
    #b convertendo celsius para fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    
    print(f"{celsius}°C → {fahrenheit}°F")

#b Mensagem de saída
print("Até mais!")