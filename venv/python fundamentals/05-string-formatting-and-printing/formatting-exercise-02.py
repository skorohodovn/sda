header1 = "Name"
header2 = "Age"
header3 = "Salary"

print(f"| {header1:15} | {header2:5} | {header3:12} | ")
print("-" * 42)
print(f"| {'John Doe':15} | {'27':<5} | {123456.00:12.2f} | ")
print(f"| {'John Wick':15} | {'40':5} | {50000.00:12.2f} | ")
print(f"| {'Jeff Bezos':15} | {'45':5} | {999999999.95:12.2f} | ")