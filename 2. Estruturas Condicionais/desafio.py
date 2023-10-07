
## DESAFIO. Você está fazendo um programa para um cinema que deseja verificar se o cliente tem direito à meia entrada. Ele terá este benefício caso:
#. Tenha mais que 60 anos
#. Tenha carteira de estudante
#. Seja deficiente
#. Tenha entre 15 e 29 anos e tenha baixa renda

idade = int(input("Qual sua idade? "))
estudante = input("Você é estudante? [S/N] ").lower()
deficiente = input("Você possui deficiência? [S/N] ").lower()
baixaRenda = input("Tem baixa renda? [S/N] ").lower()

condicao1 = idade >= 60
condicao2 = estudante == "s"
condicao3 = deficiente == "s"
condicao4 = baixaRenda == "s" and idade >= 15 and idade <= 29

if condicao1 or condicao2 or condicao3 or condicao4:
    print("Você tem direito à meia entrada!")
else:
    print("Você não tem direito à meia entrada")