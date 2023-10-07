
## 2. Peça 5 números decimais para o usuário e adicione-os em uma lista. Calcule a média dos valores e mostre o resultado, arredondado para 3 casas decimais

numeros = []

for i in range(5):
    num = float(input("Digite 5 números decimais: "))
    numeros.append(num)

somaTotal = 0

for numero in numeros:
    somaTotal = somaTotal + numero
    
media = somaTotal / len(numeros)

print(f"A média desses números é de {round(media, 3)}")