import cipher

plaintext = input('What would you like to encrypt?\n')
shift = int(input('How far would you like to shift (0 - 25)?\n'))

ciphertext = cipher.Ciphers.CaesarCipher(plaintext, shift)

print(f'Here is your plaintext shifted {shift} places\n\n{ciphertext}')