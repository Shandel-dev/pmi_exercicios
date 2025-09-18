print("Cálculo de juros simples")
cap = float(input("Capital inicial: "))
taxa = float(input("Informe a taxa de juros(em %): "))
tempo = float(input("Quantos meses de rendimento?: "))

juros = cap * (taxa / 100) * tempo
print(juros)
