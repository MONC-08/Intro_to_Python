alphabet = 'abcdefghijklmnopqrstuvwxyz'

def shift_amount(i):
    return i % 26

class TranspositionCipher(object):
    def __init__(self, key):
        self.key = key

    def encrypt_message(self, message):
        message = message.lower()
        output = ''
        for char in message:
            if char not in alphabet:
                output += char
            else:
                alpha_index = alphabet.find(char)
                output += alphabet[shift_amount(alpha_index + self.key)]
        return output

    def decrypt_message(self, message):
        output = ''
        for char in message:
            if char not in alphabet:
                output += char
            else:
                alpha_index = alphabet.find(char)
                output += alphabet[shift_amount(alpha_index - self.key)]
        return output


cipher = TranspositionCipher(5)

encrypted = cipher.encrypt_message("Learning Python is fun")
print("Encrypted:", encrypted)

decrypted = cipher.decrypt_message(encrypted)
print("Decrypted:", decrypted)
