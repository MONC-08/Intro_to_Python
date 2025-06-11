import math as m

class TranspositionCipher(object):

    def __init__(self, key):
        self.key = key

    def encrypt_message(self, message):

        # Split the message into a list of characters
        message_split = list(message.lower())
        # Calculate the message’s length
        message_length = len(message_split)
        # Initialize an empty string for the encrypted message
        message_encrypted = ''

        message_ceil = m.ceil(message_length / self.key)

        for col in range(self.key):
            for row in range(message_ceil):
                index = col + row * self.key

                if index < message_length:
                    message_encrypted +=  message_split[index]

        return message_encrypted

    def decrypt_message(self, message):
        message_split = list(message.lower())
        message_length = len(message_split)

        message_ceil = m.ceil(message_length / self.key) # number of cols

        # self.key * message_ceil -> total number of grid
        num_empty_cells = self.key * message_ceil - message_length

        # Initialize a grid of empty strings
        message_grid =[['' for _ in range(message_ceil)] for _ in range(self.key)]
        # Initialize an empty string for the decrypted message
        decrypted_message = ''
        # Declare an iterator object from the list of characters
        iterator = iter(message_split)

        # Construct nested for-loops for filling in the grid
        for i in range(self.key):
            if i < self.key - num_empty_cells:
                columns = message_ceil
            else:
                columns = message_ceil - 1

            for j in range(columns):
                message_grid[i][j] = next(iterator, None)

        # Construct nested for-loops for decrypting the message
        for j in range(message_ceil):
            for i in range(self.key):
                decrypted_message += message_grid[i][j]

        return decrypted_message

# ........................................................................ #
cipher = TranspositionCipher(6)
encrypted = cipher.encrypt_message('Learning Python is fun')
print("Encrypted message :> ",encrypted)
print()
print("Decrypted message is:> ",cipher.decrypt_message(encrypted))