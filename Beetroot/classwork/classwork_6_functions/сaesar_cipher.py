def caesar_cipher():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = input('Введіть текст латиницею: ')
    bias = (input('Введіть зміщення: '))
    try:
        bias = int(bias)
    except TypeError:
        print('Зміщення повинно бути цілим числом!')
        return None
    new_text = ''
    for char in text:
        if char.upper() in alphabet:
            ind = alphabet.index(char.upper())
            if ind + bias >= len(alphabet):
                new_char = alphabet[ind + bias - len(alphabet)]
            else:
                new_char = alphabet[ind + bias]
            new_text += new_char if char.upper() == char else new_char.lower()
        else:
            new_text += char
    print(new_text)


if __name__ == "__main__":
    caesar_cipher()
