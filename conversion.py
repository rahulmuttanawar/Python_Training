def decimal_to_binary_octal_hex(decimal_number):
    binary_representation = bin(decimal_number)
    octal_representation = oct(decimal_number)
    hexadecimal_representation = hex(decimal_number)
    return binary_representation, octal_representation, hexadecimal_representation


decimal_number = int(input("Enter a decimal number: "))
binary, octal, hexadecimal = decimal_to_binary_octal_hex(decimal_number)

print(f"Binary: {binary}")
print(f"Octal: {octal}")
print(f"Hexadecimal: {hexadecimal}")
