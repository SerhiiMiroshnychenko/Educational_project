with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
print("end.\n")

with open('text_files/filename.txt') as file_object:
    contents = file_object.read()
print(contents)
print("end.\n")

file_path = 'D:/Python/text_file.txt'
with open(file_path) as file_object:
    contents = file_object.read()
print(contents)
print("end.\n")
