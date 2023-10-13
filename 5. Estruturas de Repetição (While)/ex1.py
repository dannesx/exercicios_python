
## 1. Crie um programa que solicite um número de 0 a 10 para o usuário. Caso ele digite um número fora deste intervalo, peça para digitar outro número. Repita esse processo até receber um número válido

numero = -1

#b Enquanto o número for menor que 0 ou maior que 10...
while numero < 0 or numero > 10:
    #b ... pede um novo número para o usuário
    numero = int(input("Digite um número de 0 a 10: "))
    
print(numero)