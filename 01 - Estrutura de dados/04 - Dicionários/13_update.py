contacts = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

contacts.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contacts)  # {'guilherme@gmail.com': {'nome': 'Gui'}}

contacts.update(
    {"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
print(contacts)
# {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
