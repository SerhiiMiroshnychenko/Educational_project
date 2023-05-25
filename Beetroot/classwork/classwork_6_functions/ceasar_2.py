
def caesar_cipher():
    letter = list(range(65, 91)) + list(range(97, 123))
    text = input('Введіть текст латиницею: ')
    try:
        bias = int((input('Введіть зміщення: ')))
    except TypeError:
        print('Зміщення повинно бути цілим числом!')
        return None
    new_text = ''
    for char in text:
        if ord(char) in letter:
            new_char = chr(ord(char) + bias) if ord(char) + bias in letter\
                else chr(ord(char) + bias - 25)
        else:
            new_char = char
        new_text += new_char
    return new_text


print(caesar_cipher())
