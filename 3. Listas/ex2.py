
## 2. Cor Favorita: Faça um código que armazene uma lista de cores. Depois peça para o usuário informar sua cor favorita e informe se a cor que escolheu está na lista

cores = ["Verde", "Vermelho", "Amarelo", "Azul", "Lilás", "Rosa"]

favorita = input("Qual sua cor favorita? ").capitalize()

if favorita in cores:
    print("Sua cor está na lista! :)")
else:
    print("Sua cor não está na lista :(")