import codecs

binary_data = b'\x00\xFF\x00\xFF'
base64_data = codecs.encode(binary_data, 'base64')
print(base64_data)
