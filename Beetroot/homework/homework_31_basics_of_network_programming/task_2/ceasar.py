def caesar(text: str, bias: int):
    """
    The function that converts the text according to the Caesar cipher
    :param text: Text to convert (str)
    :param bias: The amount of character offset (int)
    :return: Text after conversion (str)
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
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
    return new_text


if __name__ == "__main__":
    res1 = caesar('Hello, Python!', 3)
    print(res1)

    res2 = caesar('Khoor, Sbwkrq!', -3)
    print(res2)
