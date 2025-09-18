nota = float(input("Informe a nota do aluno: "))

if nota >= 7:
    print("\033[32mAprovado!")
elif nota >= 5:
    print("\033[33mEm recuperação!")
else:
    print("\033[31mRecuperação")