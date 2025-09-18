ano = int(input("Digite um ano: "))
print("É bissexto!" if ano % 4 == 0 or (ano % 100 == 0 and ano % 400 == 0) else "Não é bissexto!")