class Ciphers:

    #character_index = {0 : 'a', 1 : 'b', 2 : 'c', 3 : 'd', 4 : 'e', 5 : 'f', 6 : 'g', 7 : 'h', 
    #                  8 : 'i', 9 : 'j', 10 : 'k', 11 : 'l', 12 : 'm', 13 : 'n', 14 : 'o', 
    #                  15 : 'p', 16 : 'q', 17 : 'r', 18 : 's', 19 : 't', 20 : 'u', 21 : 'v', 
    #                  22 : 'w', 23 : 'x', 24 : 'y', 25 : 'z'}

    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                  'w', 'x', 'y', 'z']
    characters_set = set(characters)

    @staticmethod
    def Caesar() -> str:

        plaintext = input('Enter plaintext: \n')
        shift = int(input('Define shift (0 - 25): '))

        ciphertext = []

        for idx, character in enumerate(plaintext.casefold()):
            capitalized = plaintext[idx].isupper()
            if character in Ciphers.characters_set and capitalized:
                ciphertext.append(Ciphers.characters[(Ciphers.characters.index(character) + shift) % len(Ciphers.characters)].capitalize())
            elif character in Ciphers.characters_set and not capitalized:
                ciphertext.append(Ciphers.characters[(Ciphers.characters.index(character) + shift) % len(Ciphers.characters)])
            else:
                ciphertext.append(character)
        
        return ''.join(ciphertext)
    
    @staticmethod
    def Vigenere() -> str:

        plaintext = input('Enter plaintext: \n')
        keyword = input('Enter keyword: ')

        ciphertext = []
        keyword_shifts = []
        character_pointer = 0

        for character in keyword.casefold():
            keyword_shifts.append(Ciphers.characters.index(character))

        for idx, character in enumerate(plaintext.casefold()):
            capitalized = plaintext[idx].isupper()
            if character in Ciphers.characters_set and capitalized:
                ciphertext.append(Ciphers.characters[(Ciphers.characters.index(character) + keyword_shifts[character_pointer % len(keyword)]) % len(Ciphers.characters)].capitalize())
                character_pointer += 1
            elif character in Ciphers.characters_set and not capitalized:
                ciphertext.append(Ciphers.characters[(Ciphers.characters.index(character) + keyword_shifts[character_pointer % len(keyword)]) % len(Ciphers.characters)])
                character_pointer += 1
            else:
                ciphertext.append(character)

        return ''.join(ciphertext) 