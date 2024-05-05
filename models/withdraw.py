class Withdraw:
  def __init__(self, value):
    self._value = value

  @property
  def value(self):
    return self._value
  
  def register(self, account):
    isSuccessfull = account.withdraw(self.value)

    if isSuccessfull:
      account.history.add_transaction(self)