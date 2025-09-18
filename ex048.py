n1 = int(input("Primeiro número: "))
maior = n1
menor = n1

n2 = int(input("Segundo número: "))
if n2 > maior:
    maior = n2
elif n2 < menor:
    menor = n2

n3 = int(input("Terceiro número: "))
if n3 > maior:
    maior = n3
elif n3 < menor:
    menor = n3

print(f"Maior número: {maior}\nMenor número: {menor}")