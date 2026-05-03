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

dic = {"joao": -5000, "maria": 10000, "pedro": -5000, "ana": -2000}

print ("Clientes:", list(dic.keys()))
print ("Dividas:", list(dic.values()))

saldo_buscado =  input("Digite o nome do cliente para verificar o saldo: ") 
saldo_buscado = saldo_buscado.lower()
saldo_buscado = saldo_buscado.strip()

if saldo_buscado in dic:
    saldo = dic[saldo_buscado]
    print(f"Saldo de {saldo_buscado}: {saldo}") 

    while True:
        opcao = input("Deseja realizar um pagamento? (s/n): ")
        if opcao.lower() == 's':
            valor_pagamento = float(input("Digite o valor do pagamento: "))
            dic[saldo_buscado] += valor_pagamento
            print(f"Novo saldo de {saldo_buscado}: {dic[saldo_buscado]}")
        elif opcao.lower() == 'n':
            print("Operação encerrada.")
            break
        else:
            print("Opção inválida. Digite 's' para sim ou 'n' para não.")

contador = 0
while True:
    print("Loop infinito")
    contador += 1
    print(f"Contador: {contador}")
    if input("Deseja sair? (s/n aperte enter): ") == "s":
        break

while True:
    print("Loop infinito")
    contador += 1
    print(f"Contador: {contador}")
    if contador >= 50:
        break

for dfg in range(10):
    print("oi")

precos = [1000, 2000, 3000, 4000, 5000]

total_imposto = 0

for i in precos:
    if i > 3000:
        imposto = 0.15
       

    elif i > 2000:
        imposto = 0.12
      

    elif i > 1000:
        imposto = 0.1
        

    else:
        imposto = 0.05

    imposto_venda = i * imposto
    print(f"O imposto a ser cobrado é de R${imposto_venda:.2f} para o preço de R${i:.2f} com um imposto de {imposto:.2%}".replace(".", ","))
    
    # total_imposto = total_imposto + imposto_venda
    total_imposto += imposto_venda

print(f"O total de imposto é de R${total_imposto:.2f}")

vendas_2025 = {"jan": 1000, "fev": 2000, "mar": 3000, "abr": 5000, "mai": 5000, "jun": 6000, "jul": 7000, "ago": 8000, "set": 9000, "out": 10000, "nov": 11000, "dez": 12000}
vendas_2026 = {"jan": 1500, "fev": 2500, "mar": 3500, "abr": 4500, "mai": 5500, "jun": 6500, "jul": 7500, "ago": 8500, "set": 9500, "out": 10500, "nov": 11500, "dez": 12500}

crescimento_total_medio = 0

for mes in vendas_2025:
    # print(mes)
    # print(vendas_2025[mes])
    valor_2025 = vendas_2025[mes]
    valor_2026 = vendas_2026[mes]
    # crescimento = ((valor_2026 - valor_2025) / valor_2025) * 100
    crescimento = (valor_2026 / valor_2025 - 1)
    print(f"Crescimento de {mes}: {crescimento:.2%}")
    crescimento_total_medio += crescimento / len(vendas_2025)
print(f"Crescimento médio total do ano: {crescimento_total_medio:.2%}")

