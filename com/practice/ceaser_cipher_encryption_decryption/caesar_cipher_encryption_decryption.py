from com.practice.ceaser_cipher_encryption_decryption.art_logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def cipher(plain_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            new_position = new_position % 26
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f'{cipher_direction}d message is {end_text}')


finished = False
while not finished:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cipher(text, shift, direction)
    finish = input('Do you want to go for again? y/n')
    if finish == 'y':
        finished = False
    else:
        finished = True
