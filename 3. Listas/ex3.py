
## 3. Lista de Reserva: crie uma lista de reserva para um restaurante. Pergunte o nome do cliente e verifique se está na lista. Se o cliente não estiver na lista, pergunte se ele deseja fazer uma reserva para outro dia. Se sim, adicione-o à uma outra lista

reserva = ["Jéssica", "Renan", "Matheus", "Ariel", "Fernanda", "Liliane"]
novaReserva = []

cliente = input("Qual seu nome? ")

if cliente in reserva:
    print("Seja bem-vindo(a)!")
else:
    escolha = input("Oh não, seu nome não está na lista! Deseja fazer uma nova reserva? [S/N] ").lower()
    
    if escolha == "s":
        novaReserva.append(cliente)
        print("Feito! Adicionamos você na reserva de amanhã")
    else:
        print("Tudo bem, até a próxima")
        
print("Reserva:", reserva)
print("Nova reserva:", novaReserva)