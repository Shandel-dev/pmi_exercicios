senha = input("Crie uma senha: ")

if len(senha) < 8:
    print("A sua senha deve ter 8 ou mais digitos!")
elif " " in senha:
    print("A sua senha não pode conter espaços!")
else:
    print("Senha válida!")
