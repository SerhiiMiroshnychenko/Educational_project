with open('sample.txt', 'w') as f:
    f.write('Sample1')
with open('sample.txt', 'r') as f:
    result = f.read()

assert result == 'Sample1'

with open('sample.txt', 'a') as f:
    f.write('Sample2')
with open('sample.txt', 'r') as f:
    result = f.read()

assert result == 'Sample1Sample2'
