number5: int = 5
number10: int = 10
number20: int = 20
number33: int = 33

print(number10.__class__, type(number20))

big5 = number5.to_bytes(2, 'big')
little5 = number5.to_bytes(2, 'little')
print(big5, little5, big5 == little5)
print(big5.__class__, type(little5))
big_5 = number5.to_bytes(1, 'big')
print(big_5, big_5 == big5)

print(number10.as_integer_ratio())

