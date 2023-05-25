def caesar_cipher():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = input('Введіть текст латиницею: ')
    try:
        bias = int((input('Введіть зміщення: ')))
    except TypeError:
        print('Зміщення повинно бути цілим числом!')
        return None
    new_text = ''
    for char in text:
        if char.upper() in alphabet:
            ind = alphabet.index(char.upper())
            new_char = alphabet[ind + bias - len(alphabet)] if ind + bias >= len(alphabet) else alphabet[ind + bias]
            if char.upper() == char:
                new_text += new_char
            else:
                new_text += new_char.lower()
        else:
            new_text += char
    return new_text


print(caesar_cipher())
