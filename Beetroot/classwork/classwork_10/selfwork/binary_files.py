b_data = bytes(range(256))
with open('../b_file', 'wb') as f:
    f.write(b_data)

with open('../b_file', 'rb') as f:
    bdata = f.read()

print(b_data == bdata)
print(type(b_data), type(bdata))
print(len(b_data), len(bdata))
print(bdata)

with open('../b_file', 'rb') as f:
    new_data_1 = f.read()
    print(type(new_data_1))
    print(type(f))
    f.seek(251, 0)
    print(f.tell())

new_data_2 = open('../b_file', 'rb')
print(type(new_data_2))
new_data_2.close()

with open('../b_file', 'rb') as f:
    f.seek(3, 1)
    print(f.tell())
    f.seek(-10, 2)
    print(f.tell())
    data_3 = f.read()
    print(data_3)

