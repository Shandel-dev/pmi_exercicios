from random import randint

print("Jogo de Adivinhação!")
numero_secreto = randint(1, 100)
acertou = False

while not acertou:
    palpite = int(input("Digite seu palpite (1-100): "))

    if palpite == numero_secreto:
        print("Parabéns!!! você acertou!")
        acertou = True
    elif palpite < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
