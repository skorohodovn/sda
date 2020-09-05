s = "This string is ynicode"

print(s.encode('utf-16le'))
print(s.encode('utf-16le').decode('utf-16be'))
