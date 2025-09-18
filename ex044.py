idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inválida!")
elif idade <= 5:
    print("Passagem grátis")
elif idade <= 12:
    print("Passagem infantil: R$10,00")
elif idade <= 59:
    print("Passagem inteira: R$20,00")
else:
    print("Passagem com desconto para idosos: R$12,00")
