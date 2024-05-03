from models.clients import clients
from utils.validator import validate_cpf, validate_address, validate_name

def create_client(name, birthday, cpf, address):

  if not validate_name(name):
    print("-"*20)
    print("Nome inválido!")
    print("-"*20)
    return

  if not validate_cpf(cpf):
    print("-"*20)
    print("CPF inválido!")
    print("-"*20)
    return

  if not validate_address(address):
    print("-"*20)
    print("Endereço inválido!")
    print("-"*20)
    return

  for client in clients:
    if client['cpf'] == cpf:
      print("-"*20)
      print("Cliente já cadastrado!")
      print("-"*20)
      return
    
  client = {
    "name": name,
    "birthday": birthday,
    "cpf": cpf,
    "address": address
  }

  clients.append(client)

  return client

def get_clients():
  returned_clients = []

  for client in clients:
    returned_clients.append(client)

  return returned_clients

def delete_client(cpf):
  for client in clients:
    if client['cpf'] == cpf:
      clients.remove(client)
      return True

  return False

