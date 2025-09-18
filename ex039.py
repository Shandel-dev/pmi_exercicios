email = "shandel@gmail.com"
senha = "123fatec"

email_input = input("Digite seu email: ")
senha_input = input("Senha: ")

if email_input == email and senha == senha_input:
    print("Login aprovado!")
else:
    print("Email ou senha incorretos!")