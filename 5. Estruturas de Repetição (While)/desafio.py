
## DESAFIO: Crie um jogo de adivinhação. Sorteie um número de 0 a 100 e armazene em uma variável. Peça um número para o jogador e verifique:
#. Se o número for maior: Mostre uma mensagem "digite um número menor"
#. Se o número for menor: Mostre uma mensagem "digite um número maior"
#. Se o número for igual: Mostre uma mensagem "Parabéns! você acertou"

import random

aleatorio = random.randint(0, 100)
palpite = -1

while palpite != aleatorio:
    palpite = int(input("Chute um número de 0 a 100: "))
    
    if palpite > aleatorio:
        print("\nMuito grande! Tente um número MENOR")
    elif palpite < aleatorio:
        print("\nPequeno demais! Tente um número MAIOR")
    else:
        print("Parabéns! você acertou!")