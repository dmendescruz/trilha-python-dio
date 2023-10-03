languages = ["python", "js", "c", "java", "csharp"]

# ["c", "js", "java", "python", "csharp"]
print(sorted(languages, key=lambda x: len(x)))
# ["python", "csharp", "java", "js", "c"]
print(sorted(languages, key=lambda x: len(x), reverse=True))
