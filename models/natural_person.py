from models.clients import Client

class Natural_Person(Client):
  def __init__(self, name, birthday, cpf, address):
    super().__init__(address)
    self.name = name
    self.birthday = birthday
    self.cpf = cpf
