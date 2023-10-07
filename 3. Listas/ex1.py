
## 1. Peça 5 números inteiros para o usuário, adicione-os a uma lista e informe:
#. A lista na ordem original
#. A lista em ordem crescente
#. O menor valor da lista
#. O maior valor da lista

n1 = int(input("N1: "))
n2 = int(input("N2: "))
n3 = int(input("N3: "))
n4 = int(input("N4: "))
n5 = int(input("N5: "))

lista = [n1, n2, n3, n4, n5]

print("Ordem original:", lista)

lista.sort()
print("Ordem crescente:", lista)

print("Menor valor:", min(lista))

print("Maior valor:", max(lista))