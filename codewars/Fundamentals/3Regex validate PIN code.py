def validate_pin(pin):
    if len(pin) < 4 or len(pin) > 6 or pin.isdigit() == False:
        return False
    return True

print(validate_pin("1234"))
print(validate_pin("12345"))
print(validate_pin("a234"))
print(validate_pin('12345'))