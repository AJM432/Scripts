import string
LETTERS = string.ascii_lowercase

# Encrypts a message using the caesar cipher, if isEncrypting=False: then decrypting
def caesarCipher(message, shift_key, isEncrypting):
    output_string = ''
    for char in message:
        if char.lower() in LETTERS:
            if isEncrypting:
                shift_pos = (LETTERS.index(char.lower()) + shift_key) % 26    # if pos less than 26 it remains the same, greater than 26 means it equals whats left over
            else: # decrypt
                shift_pos = (LETTERS.index(char.lower()) - shift_key) % 26
            
            if char.isupper() == True: output_string += LETTERS[shift_pos].upper()  # Capitalization check
            else: output_string += LETTERS[shift_pos]

        else:
            output_string += char   # characters other than letters

    return output_string


# input
secret_msg = "Hello"
key = 1

hidden = caesarCipher(message="Hello", shift_key=1, isEncrypting=True)
print(caesarCipher(hidden, key, False))

