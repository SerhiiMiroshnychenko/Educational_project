line = "Row, row,row your boat"
print(line.count('row'))
print(line.lower().count('row'))

filename = 'Alice in Wonderland.txt'
file_path = f'C:/Users/admin/Desktop/For files/{filename}'

try:
    with open(file_path, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, there is not the file {filename} by address {file_path}.")
else:
    word = input("What word to count: ")
    num_words = contents.lower().count(word)
    print(f"The file {filename} has about {num_words} words {word}.")

