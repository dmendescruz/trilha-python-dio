contact = {"nome": "Guilherme", "telefone": "3333-2221"}

contact.setdefault("nome", "Giovanna")  # "Guilherme"
print(contact)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contact.setdefault("idade", 28)  # 28
print(contact)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
