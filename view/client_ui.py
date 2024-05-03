from controllers.client_controller import create_client, get_clients, delete_client
from controllers.accounts_controller import delete_account, list_accounts

def render_client_ui():
  while(True):
    print("")
    print("")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Deletar cliente")
    print("0 - Voltar")
    option = input("Escolha uma opção: ")

    if option == "1":
      name = input("Nome: ")
      birthday = input("Data de nascimento: ")
      cpf = input("CPF: ")
      print("Exemplo de endereço: Rua, 0, Bairro, Cidade, Estado")
      address = input("Endereço: ")

      create_client(name=name, birthday=birthday, cpf=cpf, address=address)

    elif option == "2":
      print("-"*20)
      print("Lista de clientes:")
      print("")

      clients = get_clients()

      for client in clients:
        print(f"Nome: {client['name']}")
        print(f"Data de nascimento: {client['birthday']}")
        print(f"CPF: {client['cpf']}")
        print(f"Endereço: {client['address']}")
        print("-"*20)

    elif option == "3":
      print("-"*20)
      print("Deletar cliente")
      print("-"*20)

      cpf = input("Digite o CPF do cliente: ")

      has_deleted = delete_client(cpf)

      all_accounts = list_accounts()

      for account in all_accounts:
        if account['client'] == cpf:
          delete_account(cpf, account['account_number'])

      if has_deleted:
        print("-"*20)
        print("Cliente deletado com sucesso!")
        print("-"*20)
      else:
        print("-"*20)
        print("Cliente não encontrado!")
        print("-"*20)

    elif option == "0":
      break

    else:
      print("-"*20)
      print("Opção inválida!")
      print("-"*20)