import users_w as users

# CLI (Interface de Linha de Comando) para interagir com a API de usuários.

def menu():
    print("Escolha uma ação:")
    print("1 - Listar usuários")
    print("2 - Ler usuário")
    print("3 - Criar usuário")
    print("4 - Atualizar usuário")
    print("5 - Deletar usuário")
    print("0 - Sair")

while True:
    menu()
    opcao = input("Digite a opção: ")

    if opcao == "1":
        usuarios = users.list()
        print(usuarios)

    elif opcao == "2":
        user_id = input("ID do usuário: ")
        user = users.read(user_id)
        print(user)

    elif opcao == "3":
        nome = input("Nome: ")
        email = input("Email: ")
        novo = users.create({"name": nome, "email": email})
        print("Criado:", novo)

    elif opcao == "4":
        user_id = input("ID do usuário a atualizar: ")
        nome = input("Novo nome: ")
        email = input("Novo email: ")
        atualizado = users.update(user_id, {"name": nome, "email": email})
        print("Atualizado:", atualizado)

    elif opcao == "5":
        user_id = input("ID do usuário a deletar: ")
        sucesso = users.delete(user_id)
        print("Usuário deletado com sucesso!" if sucesso else "Erro ao deletar.")

    elif opcao == "0":
        print("Saindo... 👋")
        break

    else:
        print("Opção inválida.")