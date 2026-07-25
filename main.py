import cipher

user_choice = int(input('Choose a cipher...\n1: Caesar\n2: Vigenere\n'))
cipher_choice_map = {1 : cipher.Ciphers.Caesar, 2 : cipher.Ciphers.Vigenere}

ciphertext = cipher_choice_map[user_choice]()

print(f'You chose cipher {user_choice}.\nCiphertext:\n\n{ciphertext}')