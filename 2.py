senha_cadastrada = "1234"
senha = input("Digite sua senha: ")
login_cadastrado = "admin"
login = input("Digite seu login: ")
while senha != senha_cadastrada:
    print("Senha incorreta")
    senha = input("Digite a senha novamente: ")
while login != login_cadastrado:
    print("Login incorreto")
    login = input("Digite o login novamente: ")
print("Acesso Liberado")