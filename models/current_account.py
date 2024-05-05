from models.accounts import Account
from models.withdraw import Withdraw

class Current_Account(Account):
  def __init__(self, account_number, client, limit=500, withdraw_limit=3):
    super().__init__(account_number, client)
    self._limit = limit
    self._withdraw_limit = withdraw_limit
  
  def withdraw(self, value):
    withdraw_count = len(
      [transaction for transaction in self._history.transactions if transaction["type"] == Withdraw.__name__]
    )

    if withdraw_count >= self._withdraw_limit:
      print("")
      print('Limites de saque diário excedidos volte amanhã.')

    elif value > self._limit:
      print("")
      print('Valor acima do limite de saque.')
      return
    
    else:
      return super().withdraw(value)

    return False
  
  def __str__(self):
    return f"""
      Agência: {self._agency}
      Conta Corrente: {self._account_number}
      Titular: {self._client.name}
    """