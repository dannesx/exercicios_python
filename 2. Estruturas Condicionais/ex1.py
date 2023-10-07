
## 1. Peça um número para o usuário e informe se este número é positivo, negativo ou nulo

numero = int(input("Digite um número: "))

if numero < 0:
    print("Este número é negativo")
elif numero > 0:
    print("Este número é positivo")
else:
    print("Este número é nulo (0)")
    