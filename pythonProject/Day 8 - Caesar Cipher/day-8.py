alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(original_text, shift_amount):
    encrypt_text = ""
    for _ in original_text:
        if _ in alphabet:
            position = alphabet.index(_)
            new_position = (position + shift) % len(alphabet)
            encrypt_text += alphabet[new_position]
    print(encrypt_text.capitalize())

def decrypt(original_text, shift_amount):
    decrypt_text = ""
    for _ in original_text:
        if _ in alphabet:
            position = alphabet.index(_)
            new_position = (position - shift) % len(alphabet)
            decrypt_text += alphabet[new_position]
    print(decrypt_text.capitalize())
def caesar(direction):
    if direction == "encode":
        encrypt(original_text=text,shift_amount=shift)
    elif direction == "decode":
        decrypt(original_text=text,shift_amount=shift)

game_over = False
while not game_over:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    if direction not in ["encode", "decode"]:
        print("Invalid option. Please choose 'encode' or 'decode'.")
        continue
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    caesar(direction=direction)

#note: has not finished the case if user input wrong character in message