print("Cálculo de Salário Líquido")
salario_bruto = float(input("Digite o salário bruto: R$ "))

# Desconto simples de Imposto de Renda
if salario_bruto <= 2500:
    ir = 0
else:
    ir = salario_bruto * 0.15

salario_liquido = salario_bruto - ir

print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Desconto IR: R$ {ir:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")
