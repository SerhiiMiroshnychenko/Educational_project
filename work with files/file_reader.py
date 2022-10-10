print('\n\n\tExample 1')
print('-'*20 + '\n')

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

print('\n'+'-'*20)
print("end.\n")

print('\n\n\tExample 2')
print('-'*20 + '\n')

with open('text_files/filename.txt') as file_object:
    contents = file_object.read()
print(contents)

print('\n'+'-'*20)
print("end.\n")

print('\n\n\tExample 3')
print('-'*20 + '\n')

file_path = 'D:/Python/text_file.txt'
with open(file_path) as file_object:
    contents = file_object.read()
print(contents)

print('\n'+'-'*20)
print("end.\n")

print('\n\n\tExample 4')
print('-'*20 + '\n')

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)

print('\n'+'-'*20)
print("end.\n")


print('\n\n\tExample 5')
print('-'*20 + '\n')

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip(), end='')

print('\n'+'-'*20)
print("end.\n")

print('\n\n\tExample 6')
print('-'*20 + '\n')

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print('\n'+'-'*20)
print("end.\n")

print('\n\n\tExample 7')
print('-'*20 + '\n')

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

print('\n'+'-'*20)
print("end.\n")
