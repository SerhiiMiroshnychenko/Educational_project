"""Task 2"""

# Hello, world!
print("Hello, world!")

text = "Glory to Ukraine!"
# Glory to Ukraine!
print(text)

# Mariupol
print(city := 'Mariupol')
# Mariupol
print(city)
# MariupolMariupolMariupol
print(city * 3)

# False___True___2___3___4___five___6
print(False, True, 2, '3', "4", 'five', 2 * 3, sep='___')

# None
print(None)

# 	+2+4+27+4308+10+0.0
print('\n\t', 1 + 1, 2 * 2, 3 ** 3, str(4) + "308", int('5') + 5, float(True) * int(False), sep='+', end='\n' * 3)

# Beetroot_Academy
print('Academy' + "_" + "Academy")

# Academy _ Academy
print('Academy', "_", "Academy")

# Academy Academy
print("Academy", end=' ')
print('Academy', end='\n\n')

# Hello, Python! <Python is great!>
print('', end="Hello, Python! ")
print('<', ">", sep='Python is great!')

# My city is Mariupol.
print(f'My city is {city}.')

# Glory to Ukraine!#######################
print(f"{text:#<40}")
# _______________________Glory to Ukraine!
print(f"{text:_>40}")
# ...........Glory to Ukraine!............
print(f"{text:.^40}")

# Запише "My city is Mariupol." в файл my_text.txt
with open('my_text.txt', 'w') as f:
    print(f'My city is {city}.', file=f)

"""Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream."""
help(print)
