cipher_choice_map = {1 : "Caesar", 2 : "Vigenere"}

cipher_type = int(input("Choose your cipher:\n1. Caesar\n2. Vigenere\n"))
print(f"You chose the {cipher_choice_map[cipher_type]} cipher!")