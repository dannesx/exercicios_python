
## 2. Peça um número inteiro. Some todos os números até este e mostre o resultado

#b Número que o usuário escolheu
numero = int(input("Digite um numero: ")) 

#b Variável de controle da repetição
controle = 0

#b Variável para armazenar a soma dos números
soma = 0

#b Enquanto o controle for menor ou igual ao numero do usuário ...
while controle <= numero:
    #b ... incrementa a soma
    soma += controle
    # soma = soma + controle

    #b ... incrementa o controle em 1
    controle += 1
    # controle = controle + 1
    
print(f"A soma de todos os números de 0 a {numero} é {soma}")