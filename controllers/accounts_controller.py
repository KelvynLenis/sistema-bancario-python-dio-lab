from models.accounts import accounts
from constants import WITHDRAW_LIMIT, WITHDRAW_COUNT_LIMIT


def create_account(client, agency='0001'):
  account_number = len(accounts)

  acc_number_increased = account_number + 1

  account = {
    "client": client,
    "account_number": acc_number_increased,
    "agency": agency,
    "balance": 0,
    "transaction_history": [],
    "withdraw_count": 0
  }

  accounts.append(account)

  return account

def list_accounts():
  return accounts

def get_account(cpf, account_number):
  for account in accounts:
    if account['client'] == cpf and account['account_number'] == account_number:
      return account

  return None

def print_extract(balance, /, *, transaction_history):
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

def deposit(balance, value, transaction_history, /):
  if value < 0:
    print("-"*20)
    print("Valor inválido!")
    print("-"*20)
    return

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

  return [balance, transaction_history]

def withdraw(*, balance, value, transaction_history, withdraw_count):
  if balance == 0:
    print("-"*20)
    print("Não há saldo disponível para saque!")
    print("-"*20)
    return
  elif withdraw_count == WITHDRAW_COUNT_LIMIT:
    print("-"*20)
    print("Limite de saques diários atingido!")
    print("-"*20)
    return
  elif value > WITHDRAW_LIMIT:
    print("-"*20)
    print(f"Valor máximo de saque diário é de R$ {WITHDRAW_LIMIT:.2f}!")
    print("-"*20)
    return
  elif value > balance:
    print("-"*20)
    print("Saldo insuficiente!")
    print("-"*20)
    return
  
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

  return [balance, transaction_history, withdraw_count]
 
def delete_account(cpf, account_number):
  for account in accounts:
    if account['client'] == cpf and account['account_number'] == account_number:
      accounts.remove(account)
      return True

  return False