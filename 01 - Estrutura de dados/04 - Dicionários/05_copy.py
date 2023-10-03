contacts = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copy = contacts.copy()
copy["guilherme@gmail.com"] = {"nome": "Gui"}

# {"nome": "Guilherme", "telefone": "3333-2221"}
print(contacts["guilherme@gmail.com"])

print(copy["guilherme@gmail.com"])  # {"nome": "Gui"}
