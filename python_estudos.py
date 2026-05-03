def cadastrar_peca(pecas):
    nome = input("Digite a peça: ")
    pecas.append(nome)

def listar_pecas(pecas):
    for peca in pecas:
        print(peca)

def buscar_peca(pecas):
    nome = input("Digite a peça para buscar: ")
    
    if nome in pecas:
        print("Peça encontrada")
    else:
        print("Peça não encontrada")

def menu():
    pecas = []

    while True:
        print("\n1 - Cadastrar")
        print("2 - Listar")
        print("3 - Buscar")
        print("4 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_peca(pecas)
        elif opcao == "2":
            listar_pecas(pecas)
        elif opcao == "3":
            buscar_peca(pecas)
        elif opcao == "4":
            break
        else:
            print("Opção inválida")
menu()


nome = "joao paulo"
email = "emailfalsodolira@gmail.com"
#descobrir o servidor 1!nome usuario e msg usuario x foi cadastrado no email x
# io = nome.find(" ") 
# io = nome[:io].capitalize()
# print (io)
nome_usuario = nome.split()[0].capitalize()
print (f"Nome: {nome_usuario}")

servidor = email.find("@")
servidor = email[servidor+1:]
print (f"Servidor:{servidor}")
usuario = email.find("@")
usuario = email[:usuario]
print (f"Usuario:{usuario}")
print (f"Usuario {nome_usuario} foi cadastrado no email {nome_usuario}@{servidor}")

# jp = input("Digite sua senha com no minimo 8 caracteres:")
# ji = if len(jp) < 8:
#     print("A senha deve conter no minimo 8 caracteres")
# if ji true:
#     ja = input("confirme sua senha:")
# if jp == ja:
#     print("Senha cadastrada com sucesso")
# else:    
#     print("As senhas não coincidem")

# ...existing code...
jp = input("Digite sua senha com no minimo 8 caracteres:")

if len(jp) < 8:
    print("A senha deve conter no minimo 8 caracteres")
else:
    ja = input("Confirme sua senha:")
    if jp == ja:
        print("Senha cadastrada com sucesso")
    else:    
        print("As senhas não coincidem")
# ...existing code...

