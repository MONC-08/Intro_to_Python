alphabet = 'abcdefghijklmnopqrstuvwxyz'

def shift_amount(i):
    return i % 26

def encrypt(text, required_idx):
    output = ''
    text = text.lower()

    for char in text:
        if char not in alphabet:
            output = output + char
        else:
            alpha_index = alphabet.find(char)
            output = output + alphabet[shift_amount(alpha_index + required_idx)]

    return output
    

new_str = 'The cat sit on a mat'
encrypt_txt = encrypt(new_str, 5)
print(encrypt_txt)

print()
print(encrypt(encrypt_txt, -5))