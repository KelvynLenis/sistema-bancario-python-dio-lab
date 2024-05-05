from models.history import History

accounts = []

class Account:
  def __init__(self, account_number, client):
    self._balance = 0
    self._account_number = account_number
    self._agency = '001'
    self._client = client
    self._history = History()

  @property
  def balance(self):
    return self._balance
  
  @property
  def account_number(self):
    return self._account_number
  
  @property
  def agency(self):
    return self._agency

  @property
  def client(self):
    return self._client
  
  @property
  def history(self):
    return self._history

  @classmethod
  def create_account(cls, account_number, client):
    return cls(account_number, client)

  def deposit(self, value):
    if value <= 0:
      return False
    
    self._balance += value
    return True

  def withdraw(self, value):
    if value <= 0:
      print('Valor inválido')
      return False
    
    elif value > self._balance:
      print('Saldo insuficiente.')
      return False
    else:
      self._balance -= value
      
      print("")
      print("Saque realizado com sucesso!")
      print("-"*20)
      return True


