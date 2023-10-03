result = dict.fromkeys(["nome", "telefone"])
print(result)
# {"nome": None, "telefone": None}

result = dict.fromkeys(["nome", "telefone"], "vazio")
print(result)
# {"nome": "vazio", "telefone": "vazio"}
