
## 7. Escreva um programa que solicite ao usuário um número e verifique se ele é divisível por 3 e por 5 ao mesmo tempo

numero = int(input("Digite um número inteiro: "))

divisivelPor3 = numero % 3 == 0
divisivelPor5 = numero % 5 == 0

if divisivelPor3 and divisivelPor5:
    print("Este número é divisível por 3 e 5 ao mesmo tempo")
