
## 3. Escreva um programa que solicite ao usuário que digite uma temperatura em graus Fahrenheit, converta para Celsius e exiba a temperatura

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9 

print(f"A temperatura em Celsius é de {celsius}C")