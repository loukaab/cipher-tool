import cipher


plaintext = input('What would you like to encrypt?\n')
#shift = int(input('How far would you like to shift (0 - 25)?\n'))
keyword = input('What is your keyword?\n')
ciphertext = cipher.Ciphers.Vigenere(plaintext, keyword)

print(f'Here is your plaintext shifted {keyword} places\n\n{ciphertext}')