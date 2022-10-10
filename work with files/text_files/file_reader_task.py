filename = 'message.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

message_string = '\n'
for line in lines:
    message_string += line.rstrip() + ' '

print(message_string)
print(message_string.replace('dogs', 'cats'))
