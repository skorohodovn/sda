format_string_en = "%(who)s %(verb)s %(what)s %(when)s."
format_string_de = "%(who)s habe %(verb)s %(what)s %(when)s."

print(format_string_en % {'who': 'I', 'verb': 'learned', 'what': 'Python', 'when': 'today'})
print(format_string_de % {'who': 'Ich', 'verb': 'gelernt', 'what': 'Python', 'when': 'heute'})