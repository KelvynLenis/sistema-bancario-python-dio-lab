from controllers.accounts_controller import create_account
from controllers.accounts_controller import print_extract, deposit, withdraw, get_account, list_accounts, delete_account

def render_account_ui():
  while(True):
    print("-"*20)
    print("")
    print("1 - Cadastrar conta")
    print("2 - Acessar conta")
    print("3 - Listar contas")
    print("4 - Deletar conta")
    print("0 - Voltar")
    option = input("Escolha uma opção: ")

    if option == "1":
      print("-"*20)
      print("Cadastro de conta corrente")
      print("-"*20)

      client = input("Digite o CPF do cliente: ")

      account = create_account(client)


      if account:
        print("-"*20)
        print("Conta corrente cadastrada com sucesso!")
      else:
        print("-"*20)
        print("Error!")
        print("-"*20)

    elif option == "2":
      print("")
      print("Acesso a conta corrente")
      print("-"*20)

      account_number = int(input("Digite o número da conta corrente: "))
      cpf = input("Digite o CPF do cliente: ")

      account = get_account(cpf, account_number)

      if account:
        render_account_options(account)
      else:
        print("")
        print("Conta corrente não encontrada!")
        print("-"*20)

    elif option == "3":
      print("Listagem de contas correntes")
      print("-"*20)
      accounts = list_accounts()

      for account in accounts:
        print(f"Conta: {account['agency']}-{account['account_number']} | Cliente: {account['client']} | Saldo: R$ {account['balance']:.2f}")
        
    elif option == "4":
      print("Deletar conta corrente")
      print("-"*20)

      account_number = int(input("Digite o número da conta corrente: "))
      cpf = input("Digite o CPF do cliente: ")

      has_deleted = delete_account(cpf, account_number)

      if has_deleted:
        print("")
        print("Conta corrente deletada com sucesso!")
        print("-"*20)
      else:
        print("")
        print("Conta corrente não encontrada!")
        print("-"*20)

    elif option == "0":
      break
    else:
      print("")
      print("Opção inválida!")
      print("-"*20)
      continue

def render_account_options(account):
  while(True):
    print("")
    print("1 - Extrato")
    print("2 - Depositar")
    print("3 - Sacar")
    print("0 - Voltar")

    option = input("Escolha uma opção: ")

    if option == "1":
      print_extract(account.get("balance"), transaction_history=account.get("transaction_history"))
    elif option == "2":
      value = float(input("Digite o valor do depósito: "))

      balance, transaction_history = deposit(account.get("balance"), value, account.get("transaction_history"))

      account.update({"balance": balance, "transaction_history": transaction_history})
    elif option == "3":
      value = float(input("Digite o valor do saque: "))
      balance, transaction_history, withdraw_count = withdraw(balance=account.get("balance"), value=value, transaction_history=account.get("transaction_history"), withdraw_count=account.get("withdraw_count"))
    
      account.update({"balance": balance, "transaction_history": transaction_history, "withdraw_count": withdraw_count})
    elif option == "0":
      break
    else:
      print("")
      print("Opção inválida!")
      print("-"*20)
      continue