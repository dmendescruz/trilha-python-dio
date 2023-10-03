contacts = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

result = contacts.pop("guilherme@gmail.com")
print(result)
# {'nome': 'Guilherme', 'telefone': '3333-2221'}

result = contacts.pop("guilherme@gmail.com", {})  # {}
print(result)
