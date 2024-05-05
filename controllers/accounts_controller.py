from models.accounts import accounts, Account
from controllers.client_controller import get_client
from models.current_account import Current_Account
from models.deposit import Deposit
from models.withdraw import Withdraw
# from constants import WITHDRAW_LIMIT, WITHDRAW_COUNT_LIMIT


def create_account(cpf):
  account_number = len(accounts)

  acc_number_increased = account_number + 1

  account = Current_Account(acc_number_increased, cpf)

  accounts.append(account)

  return account

def list_accounts():
  return accounts

def get_account(cpf, account_number):
  for account in accounts:
    if account.client == cpf and account.account_number == account_number:
      return account

  return None

def print_extract(account):
  print("")

  transactions = account.history.transactions

  if not transactions:
    print("Nenhuma transação realizada.")
    return
  else:
    print("Extrato de transações:")
    for transaction in transactions:
      print(f'{transaction["type"]} de R${transaction["value"]}')

  print("-"*20)
  print(f"Saldo total: R$ {account.balance:.2f}")
  print("-"*20)
  

def deposit(account, value, /):
  transacao = Deposit(value)

  client = get_client(account.client)

  if not client:
    print("Cliente não encontrado")
    return

  client.make_transaction(account, transacao)

  print("")
  print("-"*20)
  print("Saldo atualizado com sucesso!")
  print("-"*20)

def withdraw(*, account, value):  
  transacao = Withdraw(value)
  
  client = get_client(account.client)
  if not client:
    print("Cliente não encontrado")
    return
  
  client.make_transaction(account, transacao)

 
def delete_account(cpf, account_number):
  for account in accounts:
    if account['client'] == cpf and account['account_number'] == account_number:
      accounts.remove(account)
      return True

  return False