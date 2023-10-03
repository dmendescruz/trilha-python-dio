contacts = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# contacts["chave"]  # KeyError

result = contacts.get("chave")  # None
print(result)

result = contacts.get("chave", {})  # {}
print(result)

result = contacts.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(result)
