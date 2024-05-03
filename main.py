from view.client_ui import render_client_ui
from view.account_ui import render_account_ui


NAME = "Snake Banking"

title = NAME.center(50, " ")

print("")
print(title)

while True:
  print("-"*20)
  print("")
  print("1 - Gerir Clientes")
  print("2 - Gerir Contas")
  print("0 - Sair")
  option = input("Escolha uma opção: ")

  if option == "1":
    render_client_ui()
  elif option == "2":
    render_account_ui()
  elif option == "0":
    break
  else:
    print("Opção inválida!")
    print("")
    continue
