def caesar_cipher():
    """Function that converts text according to Caesar's cipher"""
    letter = list(range(65, 91)) + list(range(97, 123))
    try:
        bias = int((input('Введіть зміщення: ')))
    except ValueError:
        return 'Помилка вводу: зміщення повинно бути цілим числом!'
    new_text = ''
    for char in input('Введіть текст латиницею: '):
        new_char = (chr(ord(char) + bias) if ord(char) + bias in letter
                    else chr(ord(char) + bias - 25)) if ord(char) in letter else char
        new_text += new_char
    return new_text


print(caesar_cipher())
