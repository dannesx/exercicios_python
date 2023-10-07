
## 3. Desenvolva um código que adicione 50 números inteiros de 0 a 1000 em uma lista. Depois, mostre:
#. A lista original
#. A lista em ordem crescente
#. A lista em ordem decrescente
#. O menor valor
#. O maior valor

import random

numeros = []

for i in range(50):
    aleatorio = random.randint(0, 1000)
    numeros.append(aleatorio)
    
print("Ordem original:", numeros)

numeros.sort()
print("Ordem crescente:", numeros)

numeros.sort(reverse=True)
print("Ordem decrescente:", numeros)

print("Menor valor:", min(numeros))
print("Maior valor:", max(numeros))