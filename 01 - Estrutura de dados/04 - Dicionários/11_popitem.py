contact = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
result = contact.popitem()
print(result)

# contact.popitem()  # KeyError
