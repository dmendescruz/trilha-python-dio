contacts = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

result = "guilherme@gmail.com" in contacts  # True
print(result)

result = "megui@gmail.com" in contacts  # False
print(result)

result = "idade" in contacts["guilherme@gmail.com"]  # False
print(result)

result = "telefone" in contacts["giovanna@gmail.com"]  # True
print(result)
