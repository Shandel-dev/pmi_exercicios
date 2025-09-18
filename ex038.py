caractere = input("Digite um caractere: ")
caractere.lower()

if not caractere.isalpha():
    print("Não é letra")
elif caractere in "aeiou":
    print("É vogal!")
else:
    print("É consoante!")