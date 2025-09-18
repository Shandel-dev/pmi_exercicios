valor = float(input("Digite o valor das compras: R$"))

desc = 0

if valor > 1000:
    desc = 5
elif valor > 500:
    desc = 7.5
elif valor > 100:
    desc = 10

print(f"Desconto de {desc}%")
print(f"Valor: R${valor - (valor * desc / 100)}")