
## 4. Tabuada: Escreva um código que peça um número para um usuário e mostre sua tabuada

numero = int(input("Digite um número inteiro: "))

for x in range(1, 11):
    resultado = x * numero
    print(f"{numero} X {x} = {resultado}")