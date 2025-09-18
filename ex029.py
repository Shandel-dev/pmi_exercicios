num1 = int(input("Digite o primeiro número: "))
maior = num1
menor = num1

num2 = int(input("Digite o segundo número: "))
if num2 > maior:
    maior = num2
elif num2 < menor:
    menor = num2

num3 = int(input("Digite o terceiro número: "))
if num3 > maior:
    maior = num3
elif num3 < menor:
    menor = num3

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")