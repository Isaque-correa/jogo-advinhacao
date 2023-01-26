print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")
numero_secreto = 4
chute_str = input("Digite o numero: ")
chute = int(chute_str)
print("Voce digitou ", chute)

if(numero_secreto == chute):
    print("você acertou o numero")
else:
    print("Você errou o numero")