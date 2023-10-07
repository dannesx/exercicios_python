
## 5. Faça um programa que solicite ao usuário um número inteiro e verifique se é par ou ímpar

numero = int(input("Digite um número inteiro: "))

numeroPar = numero % 2 == 0

if numeroPar:
    print("Este número é par")
else:
    print("Este número é ímpar")
    
    