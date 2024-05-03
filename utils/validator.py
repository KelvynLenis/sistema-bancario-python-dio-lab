import re

def validate_name(name):
    if name.isalpha():
        return True
    else:
        return False

def validate_cpf(cpf):  
  if cpf.isdigit():
      return True
  else:
      return False
  
def validate_address(address):
  if address.isalpha():
    return True
  else:
    return False

def validate_address(address):
    pattern = r'^\w+,\s\d+,\s\w+,\s\w+,\s\w+$'

    if re.match(pattern, address):
        return True
    else:
        return False