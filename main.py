name = "Snake Banking"
balance = 0
withdraw_limit = 500
withdraw_count_limit = 3
withdraw_count = 0

transaction_history = []

title = name.center(50, " ")

print("")
print(title)

while True:
    print("1. Extrato")
    print("2. Depositar")
    print("3. Sacar")
    print("0. Sair")

    option = input("Escolha uma opção: ")

    if option == "1":
        print("")
        print("-"*20)
        print(f"Saldo total: R$ {balance:.2f}")
        print("-"*20)

        if len(transaction_history) == 0:
          print("Nenhuma transação realizada!")
          print("")
        else:
          print("Histórico de transações:")
          print("")

          for transaction in transaction_history:

            if transaction['type'] == "deposit":
              print(f"Saldo antigo:   R$ {transaction['Previous balance']:.2f}")
              print(f"Depósito:   +R$ {transaction['Value deposited']:.2f}")
              print(f"SALDO ATUAL: R$ {transaction['Current balance']:.2f}")

            else:
              print(f"Saldo antigo:    R$ {transaction['Previous balance']:.2f}")
              print(f"Valor do saque: -R$  {transaction['Value withdrew']:.2f}")
              print(f"SALDO ATUAL:     R$ {transaction['Current balance']:.2f}")

            print("")
          print("-"*20)

    elif option == "2":
        value = float(input("Digite o valor do depósito: "))

        if value < 0:
          print("-"*20)
          print("Valor inválido!")
          print("-"*20)
          continue

        balance += value

        transaction_dict = {
          "Current balance": balance,
          "Previous balance": balance-value,
          "Value deposited": value,
          "type": "deposit"
        }

        transaction_history.append(transaction_dict)

        print("")
        print("-"*20)
        print("Saldo atualizado com sucesso!")
        print("-"*20)
    elif option == "3":
        value = float(input("Digite o valor do saque: "))

        if balance == 0:
          print("-"*20)
          print("Não há saldo disponível para saque!")
          print("-"*20)
          continue
        elif withdraw_count == withdraw_count_limit:
          print("-"*20)
          print("Limite de saques diários atingido!")
          print("-"*20)
          continue
        elif value > withdraw_limit:
          print("-"*20)
          print(f"Valor máximo de saque diário é de R$ {withdraw_limit:.2f}!")
          print("-"*20)
          continue
        elif value > balance:
          print("-"*20)
          print("Saldo insuficiente!")
          print("-"*20)
          continue
        
        balance -= value

        transaction_dict = {
          "Current balance": balance,
          "Previous balance": balance+value,
          "Value withdrew": value,
          "type": "withdraw"
        }

        transaction_history.append(transaction_dict)

        withdraw_count += 1
        print("")
        print("-"*20)
        print("Saque realizado com sucesso!")
        print(f"Saldo antigo: {balance + value}")
        print(f"Saldo atual: {balance}")
        print("-"*20)
    elif option == "0":
      break
    else:
      print("Opção inválida!")
      print("")
      continue
