
## 6. Escreva um programa que receba 3 valores e exiba o maior deles

n1 = int(input("Digite 3 números: "))
n2 = int(input("Digite 3 números: "))
n3 = int(input("Digite 3 números: "))

if n1 > n2 and n1 > n3:
    print(f"{n1} é o maior número")
elif n2 > n1 and n2 > n3:
    print(f"{n2} é o maior número")
else:
    print(f"{n3} é o maior número")
    